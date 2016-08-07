#!/bin/bash

directory=$PWD
sudo apt-get update && sudo apt-get -y install nginx
cp lights /etc/nginx/sites-available/
cd /etc/nginx/sites-enabled
ln -s ../sites-available/lights
rm /etc/nginx/sites-enabled/default

cd $directory
