import os
import sys
#print os.path.split(__file__)[:-1]+('..',)
sys.path.append(os.path.join(*os.path.split(__file__)[:-1]+('..',)))
from framework import constants as c
analyses = os.listdir(c.analyses_dir)
import framework.modules.commons

from framework.server import Meta

for d in os.walk(os.path.join(c.base_dir,"../")):
    for fn in d[2]:
        if fn == "seperator":
            os.rename(os.path.join(d[0],fn),os.path.join(d[0],"separator"))
