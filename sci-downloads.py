#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from scihub import SciHub

sh = SciHub()
SAVE_PATH = os.getcwd() + '/Desktop/'

for i in range(1, len(sys.argv)):
    # identifier can be link URL, DOI, or PMID
    identifier = str(sys.argv[i])
    # PDF Saved Path - You should change this to your own path
    sh.download(identifier=identifier, path=SAVE_PATH)
