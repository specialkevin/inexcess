inexcess: A New Sensation for Backups.
========

**inexcess** is a python backup utility that stores all backup files and revisions in GridFS.

![INXS](http://inxs.com/wp-content/uploads/2013/01/INXS-KICK2-300x280.jpg)

REQUIREMENTS
------------
* MongoDB
* PyMongo

FEATURES
----------

* Backup up specified local directories into GridFS

Installation
------------

    pip install git+git://github.com/specialkevin/inexcess.git

Setup
-----

Edit the configuration file (/etc/inexcess.conf.example) to suit your needs and then copy to remove the example.

    cp /etc/inexcess.conf.example /etc/inexcess.conf

Future Features
---------------

* Revisioning
* Limiting Number of Backups
* Backup Remote Locations via Fabric
* Restore files instead of using Mongo tools (i.e. mongofiles)
