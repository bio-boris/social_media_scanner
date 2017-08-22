# Thought experiment
### Completed
* User can log in
* User can search twitter for a query
* User can save their scheduled query
* Models for user query
* Models for query job
* Models for the results of the query job
* Deployment to amazon ec2 http://13.58.160.200
* Draft of blog post about deployment (https://medium.com/@bsadkhin/deploying-a-django-app-to-amazon-ec2-3f17a735a561)


### ToDo
* Task scheduling http://django-extensions.readthedocs.io/en/latest/jobs_scheduling.html
* Cron jobs for above tasks
* Create task to query job
* Create page to view results of query job
* Add other APIS

## Setting Up Your Users
``` python manage.py createsuperuser ```

## Testing with PyTest
* Todo

# Installing Libraries on ec2 AMI Linux
```
  yum groupinstall 'Development Tools'
  yum install libffi-devel.x86_64
  yum install zlib-devel
  yum install libjpeg-turbo-devel libpng-devel
  yum install postgresql95.x86_64 
  yum install postgresql95-contrib.x86_64
  yum install postgresql95-devel.x86_64
  yum install postgresql95-docs.x86_64
  yum install postgresql95-libs.i686
  yum install postgresql95-libs.x86_64
  yum install postgresql95-server.x86_64
  yum install postgresql95-static.x86_64
  yum install postgresql95-test.x86_64 
  yum install postgresql95-plperl.x86_64
  yum install postgresql95-plpython26.x86_64
  yum install postgresql95-plpython27.x86_64 
```

# Getting dependencies
``` virtualenv django; source django/bin/activate
 cd social_media_scanner
 pip install -U pip setuptools
 pip install -r requirements/production.txt
 pip install -r requirements.txt
 ```
 
# Postgres
```
sudo service postgresql95 initdb
sudo service postgresql95 start
sudo su postgres
createdb analyte
psql
ALTER USER postgres WITH PASSWORD '$password';
```
# WSGI Setup and deployment to amazon ec2
 Read more at https://medium.com/@bsadkhin/deploying-a-django-app-to-amazon-ec2-3f17a735a561
