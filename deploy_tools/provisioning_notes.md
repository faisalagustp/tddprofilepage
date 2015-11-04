Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
  └── SITENAME
    ├── database
    ├── source
    ├── static
    └── virtualenv

##Creating nginx config file using magic
    sed "s/SITENAME/pmpl-faisal.cloudapp.net/g" \
        deploy_tools/nginx.template.conf | sudo tee \
        /etc/nginx/sites-available/pmpl-faisal.cloudapp.net

##activating file
    sudo ln -s ../sites-available/pmpl-faisal.cloudapp.net \
    /etc/nginx/sites-enabled/pmpl-faisal.cloudapp.net

##upstart using sed
    sed "s/SITENAME/pmpl-faisal.cloudapp.net/g" \
        deploy_tools/gunicorn-upstart.template.conf | sudo tee \
        /etc/init/gunicorn-pmpl-faisal.cloudapp.net.conf
