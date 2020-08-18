#!/usr/bin/python3
"""deploy web static module"""
from datetime import datetime
from os import path
from fabric import api

api.env.user = 'ubuntu'
api.env.hosts = ['35.231.95.4', '54.175.222.196']


def do_pack():
    """
    Generates a .tgz archive from the contents of
    the web_static folder of AirBnB Clone repo
    """
    if not path.isdir("versions"):
        api.local("mkdir versions")
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    t_name = "versions/web_static_{}.tgz".format(date)
    result = api.local("tar -czvf {} web_static".format(t_name))
    if result.failed:
        return None
    return t_name


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
    """
    if not path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        just_name = file_name.split(".")[0]
        api.put(archive_path, "/tmp/")
        api.run("mkdir -p /data/web_static/releases/{}".format(just_name))
        api.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                                                        file_name, just_name))
        api.run("rm /tmp/{}".format(file_name))
        path_r = "/data/web_static/releases/"
        api.run('mv {0}{1}/web_static/* {0}{1}/'.format(path_r, just_name))
        api.run('rm -rf /data/web_static/releases/{}/web_static'.format(
                                                                just_name))
        api.run("rm -rf /data/web_static/current")
        api.run("ln -s /data/web_static/releases/{} \
                    /data/web_static/current".format(just_name))
        return True
    except:
        return False


def deploy():
    """
    Fabric script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
    """
    tgz_file = do_pack()
    if tgz_file is None:
        return False
    result_d = do_deploy(tgz_file)
    return result_d
