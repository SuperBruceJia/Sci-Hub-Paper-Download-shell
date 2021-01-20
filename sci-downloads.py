#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import getpass
from scihub import SciHub

sh = SciHub()
user = str(getpass.getuser())

for i in range(1, len(sys.argv)):
    k = i
    name = str(sys.argv[i])
    PATH = '/Users/' + user + '/Desktop/paper' + str(i) + '.pdf'

    while os.path.exists(PATH) is True:
        k += 1
        PATH = '/Users/' + user + '/Desktop/paper' + str(k) + '.pdf'

    sh.download(name, path=PATH)
