import sys, getopt,  re, os
import subprocess
from subprocess import Popen, PIPE, check_output

#######################################################################
# Name SvnAdd
# Desc: check revision 'path' of SVN for revision control
#######################################################################
def SvnVersion(path):
    result = None
    check = False
    try:
        result = check_output(["svn", "--version"], path)
        check = True
    except OSError as e:
        check = False
        print e
    
    if check:
        check = False
        ver = re.search("version\s\d+.\d+.\d+ ", result)
        if ver:
            check =  True
            print(ver.group(0))
    return check