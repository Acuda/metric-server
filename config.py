#!flask/bin/python
#-*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# WEBSERVER: Flask
SERVER_HOST_IP = '0.0.0.0'
SERVER_PORT = 8042
SERVER_DEBUG_ENABLED = True

# DATABASE: SQLAlchemy with SQLITE
SQLALCHEMY_DATABASE_NAME = 'app.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                      SQLALCHEMY_DATABASE_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')