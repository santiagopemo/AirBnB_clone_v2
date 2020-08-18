#!/usr/bin/python3
"""Do clean web static module"""
from datetime import datetime
import os
from fabric import api

api.env.user = 'ubuntu'
api.env.hosts = ['35.231.95.4', '54.175.222.196']


def do_clean(number=0):
    """
    Fabric script (based on the file 3-deploy_web_static.py) that
    deletes out-of-date archives, using the function do_clean
    """
    number = int(number)
    if number == 0:
        number = 1
    for i, d in enumerate(sorted(os.listdir("versions"))):
        if i >= number:
            api.local("rm /versions/{}".format(d))
    versions = api.run("ls /data/web_static/releases").split()
    for i, d in enumerate(sorted(versions)):
        if i >= number and d != 'test':
            api.run("rm -R /data/web_static/releases/{}".format(d))
