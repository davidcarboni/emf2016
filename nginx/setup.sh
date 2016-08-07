#!/bin/bash

directory=$PWD
sudo apt-get update && sudo apt-get -y install nginx
sudo cp lights /etc/nginx/sites-available/
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/lights
sudo rm /etc/nginx/sites-enabled/default

cd $directory
sudo nginx -t
sudo service nginx reload
