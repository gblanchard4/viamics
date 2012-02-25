import os
import sys
import cPickle
import copy

#this line is utter cargo-cult. I have no idea why it is here
sys.path.append(os.path.join(*os.path.split(__file__)[:-1]+('..',)))

from framework import constants as c
from framework.server import Meta
import framework.tools.taxons as taxons

analyses = os.listdir(c.analyses_dir)

for a in analyses:
    p = Meta(a)
    d = cPickle.load(open(p.files.samples_serialized_file_path))
    l = cPickle.load(open(p.files.otu_library_file_path))
    
    map_dirs = os.listdir(os.path.join(c.analyses_dir,a,"maps"))
    for m in map_dirs:
	mf = os.path.join(c.analyses_dir,
			  a,
			  c.sample_maps_dir_name,
			  m,
			  c.sample_map_file_name)
        sd = os.path.join(c.analyses_dir,
			  a,
	                  c.sample_maps_dir_name,
	                  m,
	                  c.sample_map_taxon_charts_dir_name)
	for r in c.ranks[p.type]:
	    tpd = taxons.get_t_p_values_dict_for_subset(
		d, 
		l, 
		mf, 
		ranks = copy.deepcopy(c.ranks[p.type]))
	    
	    taxons.generate_data_files(d,tpd,mf,rank=r,save_dir=sd)
    
