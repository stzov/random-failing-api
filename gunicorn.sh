#!/bin/sh
/home/app/.local/bin/gunicorn api:app -b 0.0.0.0:5678 -c gunicorn.conf.py