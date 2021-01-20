import sys
import getpass
from scihub import SciHub

sh = SciHub()
user = getpass.getuser()

if len(sys.argv) == 2:
    name = str(sys.argv[1])
    result = sh.download(name, path='/Users/'+ str(user) + '/Desktop/paper.pdf')
else:
    for i in range(1, len(sys.argv)):
        name = str(sys.argv[i])
        result = sh.download(name, path='/Users/' + str(user) + '/Desktop/paper' + str(i) + '.pdf')
