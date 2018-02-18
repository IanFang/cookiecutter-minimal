"""
Automate frequently used tasks
"""

from fabric.api import *
import os
import os.path

work_path = os.path.dirname(os.path.realpath(__file__))

def push():
    with cd(work_path):
        local('git checkout master')
        local('git push origin master')

def pull():
    with cd(work_path):
        local('git checkout master')
        local('git pull origin master')
