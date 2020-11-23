import sys, getopt,  re, os
import subprocess
from subprocess import Popen, PIPE, check_output

#######################################################################
# Name SvnAdd
# Desc: Add 'path' to SVN for revision control
#######################################################################
def SvnAdd(path):
    result = None
    try:
        result = check_output(["svn", "add", path],
                 stderr = open(os.devnull, 'w'))
    except subprocess.CalledProcessError as e:
        print e
        result = None
    
    return result