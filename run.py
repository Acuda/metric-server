#!flask/bin/python
#-*- coding: utf-8 -*-

import os
import errno
import imp

from app import app
import config

def run():
    app.run(host=config.SERVER_HOST_IP, port=config.SERVER_PORT,
            debug=config.SERVER_DEBUG_ENABLED)

def create_structure():
    # create default directories if not exist
    dirlist = ['app/static/resources', 'app/templates']

    try:
        for dir in dirlist:
            os.makedirs(dir)
    except OSError as ex:
        if ex.errno is not errno.EEXIST:
            raise

    # create database if not exist
    if not os.path.isfile(config.SQLALCHEMY_DATABASE_NAME):
        print 'Create new Database'
        mod = imp.load_module('db_create', *imp.find_module('db_create'))
        mod.db_create()

        print 'Migrate models'
        mod = imp.load_module('db_migrate', *imp.find_module('db_migrate'))
        mod.db_migrate()

if __name__ == '__main__':
    create_structure()
    run()