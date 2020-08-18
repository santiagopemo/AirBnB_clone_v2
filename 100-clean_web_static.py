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
    tgz_files = sorted(os.listdir("versions"))
    for f in range(number):
        tgz_files.pop()
    with api.lcd("versions"):
        for f in tgz_files:
            api.local("rm {}".format(f))

    with cd("/data/web_static/releases"):
        versions_files = api.run("ls -tr").split()
        tgz_files = []
        for f in versions_files:
            if "web_static" in f:
                tgz_files.append(f)
        for f in range(number):
            tgz_files.pop()
        for f in tgz_files:
            api.run("rm -rf ./{}".format(f))
