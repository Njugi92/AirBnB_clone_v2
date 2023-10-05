#!/usr/bin/python3
"""Fabric script based on 2-do_deploy_web_static.py
that creates and distributes archives to your web servers
using the function deploy
"""


from fabric.api import *
from datetime import datetime
from os.path import exists
# do_pack = __import__('1-pack_web_static').do_pack
# do_deploy = __import__('2-do_deploy_web_static').do_deploy
# ['ip web-01', 'ip web-02']
env.hosts = ['52.204.97.34', '34.203.75.101']


def do_pack():
    """This generates .tgz archive from web static folder"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """To distribute archive to your web servers"""
    if exists(archive_path) is False:
        return False
