#!/usr/bin/env python
# -*- coding: utf-8 *-*

from ConfigParser import ConfigParser
from bottle import route, get, post, request, run, template, redirect
import os

config = ConfigParser()
config.read(os.path.join("config.ini"))

log_file = config.get("app", "log")
port = config.getint("app", "port")

app_path = config.get("deploy", "path")
branch = config.get("deploy", "branch")
deploy_cmd = config.get("deploy", "command")

@post('/')
def main():
    try:
        project = request.json.get('project')
        print "project:",project
        object_kind = request.json.get('object_kind')
        print "object_kind:",object_kind
        ref = request.json.get('ref')
        print "ref:",ref
        if branch in ref:
            command_cd = "cd " + app_path + " && "

            command_pull = command_cd + " git pull origin " + branch
            print "Ejecutando: " + command_pull
            os.system(command_pull)

            command_restart = command_cd + deploy_cmd
            print "Ejecutando " + command_restart
            os.system(command_restart)
    except:
        print 'Hubo error'

@get('/')
def index():
    return "Hello"

if __name__=="__main__":
    run(host='0.0.0.0', reloader=True, debug=True, port=port)
