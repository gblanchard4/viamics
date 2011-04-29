#!/usr/bin/python

# TODO: 
#   
#   - Right now it only supports Debian-Based Linux Distrobutrions that use apt-get to install software packages. We should add support for other OSes (Not you, Windows!)
#   - rdp_classifier should not download if it is already there...likewise it shouldn't unzip if already unzipped.
#   - Change all occurances of path creations to use os.join()
#   - .htaccess install
#   - I feel dirty for how I solved the permissions issues I've had. I could definitely use advice on that.

import os, sys

print "Thank you for your interest in installing Viamics!\n"

supported_platforms = {"linux2": True, "darwin": True}

# Only works on linux and (soon) OS X :)
platform = sys.platform
if not platform in supported_platforms:
    print "Sorry, but right now this script only works in Debian-Based Linux Distros using apt-get!\nShutting down...Goodbye!\n"
    sys.exit(0)


if platform == "darwin":
    import stat, time
    os.system('ruby -e \"$(curl -fsSLk https://gist.github.com/raw/323731/install_homebrew.rb)\" && brew install git && brew install gfortran && brew install r && brew install python && brew install PIL && echo -e \"\nexport PATH=/usr/local/share/python:/usr/local/bin:$PATH\" >> ~/.profile')
    os.system("/usr/local/share/python/easy_install pip && /usr/local/share/python/pip install --upgrade distribute && /usr/local/share/python/pip install rpy2 && /usr/local/share/python/pip install numpy && /usr/local/share/python/pip install scipy && /usr/local/share/python/pip install django && /usr/local/share/python/pip install cogent && export LDFLAGS=\'-L/usr/X11/lib\' && export CFLAGS=\'-I/usr/X11/include -I/usr/X11/include/freetype2 -I/usr/X11/include/libpng12\' && /usr/local/share/python/pip install http://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.0.1/matplotlib-1.0.1.tar.gz && /usr/local/share/python/pip install pil")
    file_name = 'temp' + str(int(time.time())) + '.py'
    f = open(file_name, "w")

    script = """#!/usr/local/bin/python
import os, sys, urllib, zipfile, commands
def reporthook(blocks_read, block_size, total_size): 
    print '% 3.1f%% of %d bytes\\r' % (min(100, float(blocks_read * block_size) / total_size * 100), total_size),
    sys.stdout.flush()

print 'Thank you for your interest in installing Viamics!\\n'


#
# Check if we have super user permissions by checking if we can write to apache2 folder.
# We eventually need super user permissions, but having it all the way through the script 
# will cause ownership conflicts for things we'd like to have without super user permissions.
# Because of this, we prevent the script from running with super user permissions.
#

try:
    temp = '/etc/test.permissions.file'
    test = open(temp,'wr')
    test.close()
    if os.path.exists(temp):
        os.remove(test.name)
        print 'Please do not execute this script with super user privelleges.\\nGoodbye ...\\n'
        sys.exit(0)

except IOError:
    pass



#
# Porbably unecessary, but double check that rpy2 is properly installed before we go diving in with rpy2 calls.
#

try:
    import rpy2.robjects as R

except:
    print ' FAILED!\\nPython Module - \\'rpy2\\' was unable to be installed. Please install this module manually.\\n'
    sys.exit(0)

#
# Install R packages
#

print 'Installing R packages...'

# Set the CRAN to default repository (this may need to be changed to ensure that if this repo goes down, we have another option)
# And second command in script updates all current packages in R...Interesting note: as of 2/28/11 a fresh install of R does in fact have packages requiring updates.

script_commands = ['options(repos=c(CRAN=\\'http://streaming.stat.iastate.edu/CRAN/\\'))\\n','update.packages(ask=FALSE)\\n']

# Check for each required R package. If they are not found, add them to a temporary R script file to be installed later.
from rpy2.robjects.packages import importr

def installed(r_pkg):
    try:
        importr(r_pkg)
        return True
    except:
        return False

r_pkgs =  ['gtools','gdata','caTools','bitops','gplots']

for pkg in r_pkgs:
    if not installed(pkg):
        script_commands.append("install.packages('"+pkg+"')\\n")

script_commands.append('quit()\\n')

f = open('rpackages.script', 'w')
f.writelines(script_commands)
f.close()

# Execute R script file
try:
    os.system('/usr/local/bin/R -f %s' % f.name)
except:
    print 'Can\\'t find %s!' % f.name
    os._exit(os.EX_NOTFOUND)
    print 'FAILED!\\nThere was an error installing the packages required for R!\\n'

# Remove Temp R Script file
os.remove(f.name)

# Ensure that R libraries can be found

fail_string = 'FAILED!\\n Please try to manual install the following R packages:\\n\\n'
failed = False

for pkg in r_pkgs:
    if not installed(pkg):
        fail_string = fail_string + '\\t'+pkg+'\\n'
        failed = True
if failed:
    print fail_string+'GOODBYE'
    sys.exit(0)


#
# Download and unzip rdp_classifier
#
# Note: Uses system call to unzip to unzip. I was unable to get zipfile library to work without OSError. This may be a bug in library.

print 'Downloading RDP Classifier...\\n'

rdp_name = 'rdp_classifier_2.2'
rdp_zip_name = rdp_name + '.zip'

# SHOULDN'T DOWNLOAD IF ALREADY THERE!

try:
    urllib.urlretrieve('http://downloads.sourceforge.net/project/rdp-classifier/rdp-classifier/rdp_classifier_2.2.zip', rdp_zip_name, reporthook)
except:
    if not rdp_zip_name in os.listdir('.'):
        print 'Unable to find %s from sourceforge.net. Our link may be out-of-date, please manually download this file to this directory and execute this script again!\\nGoodbye...\\n' % (rdp_zip_name)
        sys.exit(0)

if zipfile.is_zipfile(rdp_zip_name):
    # Possibly check if the folder is already there?
    try:
        os.system('unzip %s' % rdp_zip_name)
    except:
        print 'There was an error unzipping %s\\n' % rdp_zip_name
#
# Clone Viamics
#

os.system('/usr/local/bin/git clone git://github.com/meren/viamics.git')

#
# Create proper config.py
#

# get the working directory
current_dir = os.getcwd()

#### =====>change to os.join()<=====
# these are the proper paths to be used in the new config.py file
rdp_path = current_dir + '/' + rdp_name # /current/working/directory/rdp_classifier_2.2
framework_path = current_dir +'/viamics/framework'

# these are the placeholders in the default config file to be replaced
rdp_placeholder = '/path/to/rdp/classifier'
framework_placeholder = '/path/to/framework'

# copy the default config file
template_config = open(framework_path + '/config-default.py', 'r')
text = template_config.read()
template_config.close()

# write the proper config file
config = open(framework_path + '/config.py', 'w')
config.write(text.replace(rdp_placeholder, rdp_path).replace(framework_placeholder, framework_path))
config.close()"""
     
    f.write(script)
    f.close()
    os.system("chmod 777 "+file_name)
    os.system("./"+file_name)
    os.remove(file_name)

elif platform == "linux2":
    import urllib, zipfile
    # Check if we have super user permissions by checking if we can write to apache2 folder.
    # We eventually need super user permissions, but having it all the way through the script 
    # will cause ownership conflicts for things we'd like to have without super user permissions.
    # Because of this, we prevent the script from running with super user permissions.
    try:
        temp = "/etc/test.permissions.file"
        test = open(temp,"wr")
        test.close()
        if os.path.exists(temp):
            os.remove(test.name)
            print "Please do not execute this script with super user privelleges.\nGoodbye ...\n"
            sys.exit(0)
    
    except IOError:
        pass
    
    # install the entire apt-get repository...or at least make sure that everything we need is there!
    os.system('sudo apt-get install gcj-4.5-jre-headless git unzip python-matplotlib python-scipy r-base r-recommended python-rpy2 python-setuptools python-dev python-django apache2 libapache2-mod-python')
    
    # Porbably unecessary, but double check that rpy2 is properly installed before we go diving in with rpy2 calls.
    try:
        import rpy2.robjects as R
    except:
        print "Python Module - 'rpy2' - was not properly installed.\nRe-Attempting apt-get install..."
        os.system("sudo apt-get install python-rpy2")
        try:
            import rpy2.robjects as R        
        except:
            print " FAILED!\nPython Module - 'rpy2' was unable to be installed. Please install this module manually.\n"
            sys.exit(0)
    # Install R packages
    print 'Installing R packages...'
    
    # Set the CRAN to default repository (this may need to be changed to ensure that if this repo goes down, we have another option)
    # And second command in script updates all current packages in R...Interesting note: as of 2/28/11 a fresh install of R does in fact have packages requiring updates.
    script_commands = ["options(repos=c(CRAN=\"http://streaming.stat.iastate.edu/CRAN/\"))\n","update.packages(ask=FALSE)\n"]
    
    # Check for each required R package. If they are not found, add them to a temporary R script file to be installed later.
    from rpy2.robjects.packages import importr
    
    def installed(r_pkg):
        try:
            importr(r_pkg)
            return True
        except:
            return False
    
    r_pkgs =  ['gtools','gdata','caTools','bitops','gplots']
    
    for pkg in r_pkgs:
        if not installed(pkg):
            script_commands.append("install.packages('"+pkg+"')\n")
    
    script_commands.append("quit()\n")
    
    f = open("rpackages.script", "w")
    f.writelines(script_commands)
    f.close()
    
    # Execute R script file
    try:
        os.system("sudo R -f %s" % f.name)
    except:
        print "Can't find %s!" % f.name
        sys.exit(0)
        print "FAILED!\nThere was an error installing the packages required for R!\n"
    
    # Remove Temp R Script file
    os.remove(f.name)
    
    # Ensure that R libraries can be found
    fail_string = "FAILED!\n Please try to manual install the following R packages:\n\n"
    failed = False
    
    for pkg in r_pkgs:
        if not installed(pkg):
            fail_string = fail_string + "\t"+pkg+"\n"
            failed = True
    if failed:
        print fail_string+"GOODBYE"
        sys.exit(0)
    
    # Download and unzip rdp_classifier
    # Note: Uses system call to unzip to unzip. I was unable to get zipfile library to work without OSError. This may be a bug in library.
    
    print "Downloading RDP Classifier...\n"
    
    rdp_name = "rdp_classifier_2.2"
    rdp_zip_name = rdp_name + ".zip"
    
    # SHOULDN'T DOWNLOAD IF ALREADY THERE!
    def reporthook(blocks_read, block_size, total_size): 
        print "% 3.1f%% of %d bytes\r" % (min(100, float(blocks_read * block_size) / total_size * 100), total_size),
        sys.stdout.flush()
    
    try:
        urllib.urlretrieve("http://downloads.sourceforge.net/project/rdp-classifier/rdp-classifier/rdp_classifier_2.2.zip", rdp_zip_name, reporthook)
    except:
        if not rdp_zip_name in os.listdir("."):
            print "Unable to find %s from sourceforge.net. Our link may be out-of-date, please manually download this file to this directory and execute this script again!\nGoodbye...\n" % rdp_zip_name
            sys.exit(0)
    if zipfile.is_zipfile(rdp_zip_name):
        # Possibly check if the folder is already there?
        try:
            os.system("unzip %s" % rdp_zip_name)
        except:
            print "There was an error unzipping %s\n" % rdp_zip_name
    
    # Install pip for installation of cogent
    try:
        os.system("sudo easy_install -U pip")
    except:
        print "Unable to install pip. Please do so manually\n"
    
    # Install cogent
    cogent_file = open("cogent-requirements.txt", "w")
    cogent_file.writelines(["cogent\nnumpy>=1.3.0"])
    cogent_file.close()
    
    os.system("DONT_USE_PYREX=1")
    try:
        os.system("sudo pip install -r %s" % cogent_file.name)
    except:
        print "Unable to install cogent!\n"
    try:
        os.rm(cogent_file.name)
    except:
        pass
    
    #
    # Clone Viamics
    #
    
    os.system("git clone git://github.com/meren/viamics.git")
    
    #
    # Create proper config.py
    #
    
    # get the working directory
    current_dir = os.getcwd()
    
    #### =====>change to os.join()<=====
    # these are the proper paths to be used in the new config.py file
    rdp_path = current_dir + "/" + rdp_name # /current/working/directory/rdp_classifier_2.2
    framework_path = current_dir +"/viamics/framework"
    
    # these are the placeholders in the default config file to be replaced
    rdp_placeholder = "/path/to/rdp/classifier"
    framework_placeholder = "/path/to/framework"
    
    # copy the default config file
    template_config = open(framework_path + "/config-default.py", "r")
    text = template_config.read()
    template_config.close()
    
    # write the proper config file
    config = open(framework_path + "/config.py", "w")
    config.write(text.replace(rdp_placeholder, rdp_path).replace(framework_placeholder, framework_path))
    config.close()
    
    #
    # Make temp/errors/analyses folders 
    #
    
    tmp = framework_path + "/tmp"
    errors = framework_path + "/errors"
    analyses = framework_path + "/analyses"
    
    os.mkdir(tmp)
    os.mkdir(errors)
    os.mkdir(analyses)
    
    #
    # Change apache config file so that all instances of 'AllowOverride None' -> 'AllowOverride All'
    #
    
    elevated_script = open("elevated.py", "w")
    elevated_text = """#!/usr/bin/python
    import os
    original_text = "AllowOverride None"
    new_text = "AllowOverride All"
    
    apache_file_path = "/etc/apache2/sites-enabled/000-default"
    apache_file = open(apache_file_path, "r")
    
    text = apache_file.read()
    apache_file.close()
    apache_file = open(apache_file_path, "w")
    apache_file.write(text.replace(original_text, new_text))
    apache_file.close()
    """
    elevated_script.write(elevated_text)
    elevated_script.close()
    os.chmod('elevated.py', 777)
    os.system('sudo ./elevated.py')
    os.remove('elevated.py')

print "SUCCESS!\n"
    

