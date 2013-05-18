#!/bin/bash

virtualenv virtual_env
cd virtual_env
source bin/virtual_env
sudo apt-get install libxml2-dev libxlst-dev libevent-dev
pip install -r ../requirements.txt
