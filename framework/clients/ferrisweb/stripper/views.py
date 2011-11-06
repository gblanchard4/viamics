import os
import subprocess
import shlex
import hashlib
from forms import RunStripperForm
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

stripper_cmd = "%(stripper)s %(keyfile)s %(fasta)s %(prefix)s"
Xstrip = "/home/ferris/Desktop/viamics/framework/clients/ferrisweb/stripper/Xstrip.pl"
J = os.path.join

def strip_split(request):
    if request.method == 'POST':
        form = RunStripperForm(request.POST, request.FILES)
        return run_stripper(request.FILES['fasta'],request.FILES['keys'])
    else:
        f = RunStripperForm()
        return HttpResponse("""<html><head><title>Primer/Barcode cleaner</title></head><body><form enctype="multipart/form-data" method="post">%s<input type='submit' /></form></body></html> """ % f.as_table())

def run_stripper(fasta_file, key_file):
    h = hashlib.sha1()
    h.update(fasta_file.read())
    filehash = h.hexdigest()
    fasta_file.seek(0)
    fasta_tmp = J('/tmp',filehash+'_seqs.fas')
    key_tmp = J('/tmp',filehash+'_key')
    with open(fasta_tmp,'w') as f:
        f.write(fasta_file.read())
    with open(key_tmp,'w') as f:
        f.write(key_file.read())
    
    os.chdir('/tmp')

    cmd = stripper_cmd % {'keyfile':key_tmp,'fasta':fasta_tmp, 'prefix':filehash, 'stripper':Xstrip}
    #import pdb; pdb.set_trace()
    subprocess.call(shlex.split(str(cmd)))

    ids = filter(lambda i: i.startswith(filehash),os.listdir('.'))
    real_ids = [i.strip(filehash) for i in ids]

    for i,r in zip(ids,real_ids):
        os.rename(i,r)

    zipfile = J('/tmp','all_samples.zip')
    try:
        os.remove(zipfile)
    except:
        pass
    args = ['zip',zipfile]+[ J('/tmp',i) for i in real_ids]
    subprocess.call(args)
    response = HttpResponse(FileWrapper(open(zipfile)), content_type='application/zip')
    os.remove(zipfile)
    for i in real_ids:
        os.remove(J('/tmp',i))
    response['Content-Disposition'] = 'attachment; filename=all_samples.zip'
    return response
