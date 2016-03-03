#!/usr/bin/env python
# -*- coding: utf-8 *-*

from ConfigParser import ConfigParser
from bottle import route, get, post, request, run, template, redirect

config = ConfigParser()
config.read(os.path.join("config.ini"))

log_file = config.get("app", "log")
port = config.getint("app", "port")

app_path = config.get("deploy", "path")
branch = config.get("deploy", "branch")
command = config.get("deploy", "command")

@post('/')
def main():
    try:
        project = request.json.get('project')
        print "project:",project
        object_kind = request.json.get('object_kind')
        print "object_kind:",object_kind
        ref = request.json.get('ref')
        print "ref:",ref
    except:
        print 'Hubo error'

if __name__=="__main__":
    run(host='localhost', reloader=True, debug=True, port=port)
