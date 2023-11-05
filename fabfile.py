#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
the contents of the web_static folder of AirBnB clone repo
using the function do_pack
"""

from fabric.api import run

def do_pack():
    run('uname -a')
