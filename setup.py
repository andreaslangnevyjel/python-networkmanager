#!/usr/bin/python3-mwct -Otu
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="python-networkmanager",
    version="2.2",
    author="Dennis Kaarsemaker",
    author_email="dennis@kaarsemaker.net",
    url="http://github.com/seveas/python-networkmanager",
    description="Easy communication with NetworkManager",
    py_modules=["NetworkManager"],
    install_requires=["dbus-python", "lxml"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: zlib/libpng License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking",
    ],
)
