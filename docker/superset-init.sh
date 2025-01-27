#!/bin/bash

# create Admin user, you can read these values from env or anywhere else possible
superset fab create-admin --username "admin" --firstname Superset --lastname Admin --email "john@cameronfoundation.org" --password "admin"

# Upgrading Superset metastore
superset db upgrade

# setup roles and permissions
superset superset init

#todo Need to start Celery

# Starting server
/bin/bash -c /usr/bin/run-server.sh
