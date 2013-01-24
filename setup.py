import os
from setuptools import setup

setup(
    name = "inexcess",
    version = "0.0.1",
    author = "Kevin Harriss",
    author_email = "special.kevin@gmail.com",
    description = ("A backup utility using GridFS."),
    license = "BSD",
    keywords = "backup gridfs",
    url = "http://packages.python.org/inexcess",
    packages=['inexcess',],
    scripts=['bin/wander'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],

    install_requires = [],
)
