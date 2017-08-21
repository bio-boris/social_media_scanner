analyte
=======

Analyte

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd analyte
    celery -A analyte.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------
   
   yum groupinstall 'Development Tools'
   
   yum install libffi-devel.x86_64
   
   sudo yum install zlib-devel
      
   sudo yum install libjpeg-turbo-devel libpng-devel



   yum install postgresql95.x86_64 
   
   yum install postgresql95-contrib.x86_64
   
   yum install postgresql95-devel.x86_64
   
   yum install postgresql95-docs.x86_64
   
   yum install postgresql95-libs.i686
   
   yum install postgresql95-libs.x86_64

   yum install postgresql95-server.x86_64 : The programs needed to create and run a PostgreSQL server
   
   yum install postgresql95-static.x86_64 : Statically linked PostgreSQL libraries
   
   yum install postgresql95-test.x86_64 : The test suite distributed with PostgreSQL

   yum install postgresql95-plperl.x86_64

   yum install postgresql95-plpython26.x86_64

   yum install postgresql95-plpython27.x86_64 

The following details how to deploy this application.

  virtualenv django; source django/bin/activate
  cd social_media_scanner

#pip install setuptools --upgrade

  pip install -U pip setuptools
  pip install -r requirements/production.txt
  pip install -r requirements.txt

Postgres
-----------
sudo service postgresql95 initdb
sudo service postgresql95 start

sudo su postgres
createdb analyte




psql
ALTER USER postgres WITH PASSWORD 'password';





https://medium.com/@bsadkhin/deploying-a-django-app-to-amazon-ec2-3f17a735a561



