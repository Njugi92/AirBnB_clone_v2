#!/usr/bin/python3
"""A fabric script based on 1-pack_web_static.py that distributes
an archive to your web servers using function do_deploy
"""


from fabric.api import *
from datetime import datetime
from os.path import exists


# [<ip web-01>, <ip web-02>]
env.hosts = ['52.204.97.34', '34.203.75.101']


def do_deploy(archive_path):
    """This distributes archive to your web servers"""
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    # curr = 'data/web_static/current'
    tmp = "/tmp/" + filename

    try:
        # Uploading archive to tmp dir of web server
        put(archive_path, "/tmp/")
        # Uncompress the archive to /data/web_static/releases/
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {} /".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/data/web_static/* {}/".format(no_tgz, no_tgz))
