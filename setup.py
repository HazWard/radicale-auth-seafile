#!/usr/bin/env python3

from setuptools import setup

setup(
    name = "radicale_auth_seafile",
    version = "0.1.3",
    author = "HazWard",
    description = ("Authenticate Radicale 2 requests against Seafile"),
    license = "GPLv3",
    keywords = "radicale seafile auth",
    url = "https://github.com/hazward/radicale-auth-seafile",
    packages = ["radicale_auth_seafile"],
    install_requires = [
        "requests",
    ],
)
