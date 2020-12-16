#!/usr/bin/env python3
"""
By: Marcus Chan
Updated : 2020-08-20
Purpose: create a auto updating package when used
Libraries: gitPython, ([os,subprocess] should already be installed)
pip install gitPython <- install gitPython (assuming you are using pip to install)
"""

import os
# import git
# import subprocess
#
# print("Pulling the most recent version from GitHub")
# try:
#     gitdir = os.getcwd() # gets the current directory
#
#     #The next 2 lines pulls from the git directory
#     g = git.cmd.Git(gitdir) #this should indicate where the git directory is based on the git folder in the directory
#     g.pull()# command that actually pull the code from github
# except:
#     print("Attempt at pulling recent value has failed, please check git repository")
