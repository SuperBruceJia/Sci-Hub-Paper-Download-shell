# -*- coding: utf-8 -*-

import sys
import getpass
from scihub import SciHub

sh = SciHub()
user = str(getpass.getuser())

for i in range(1, len(sys.argv)):
    name = str(sys.argv[i])
    result = sh.download(name, path='/Users/' + user + '/Desktop/' + str(i) + '.pdf')

