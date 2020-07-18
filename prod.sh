#!/bin/bash

gunicorn --workers=1 wsgi:app
