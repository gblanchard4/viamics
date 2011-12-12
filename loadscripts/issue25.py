import os
import sys
#print os.path.split(__file__)[:-1]+('..',)
sys.path.append(os.path.join(*os.path.split(__file__)[:-1]+('..',)))
from framework import constants as c
analyses = os.listdir(c.analyses_dir)
import framework.modules.commons

from framework.server import Meta
metas = []

for a in analyses:
    p = Meta(a)
    metas.append(p)
    for m in os.listdir(os.path.join(c.analyses_dir,a,c.sample_maps_dir_name)):
        p.dirs.change_current_sample_map_instance(p.files,m)
        framework.modules.commons.category_map(p)

for p in metas:
    framework.modules.commons.env_file(p)
