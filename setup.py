# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = {}
with open("yoti_python_sandbox/version.py") as fp:
    exec(fp.read(), version)

long_description = (
    "This package contains the tools you need to quickly "
    "integrate your Python back-end tests with Yoti sandbox services, "
    "so you can test integrations with different Yoti services without "
    "using real data."
)

setup(
    name="yoti-sandbox",
    version=version["__version__"],
    packages=find_packages(include=["yoti_python_sandbox", "yoti_python_sandbox.*"]),
    license="MIT",
    description="The Yoti Python Sandbox SDK, providing API support for sandbox services",
    long_description=long_description,
    url="https://github.com/getyoti/yoti-python-sdk-sandbox",
    author="Yoti",
    author_email="websdk@yoti.com",
    install_requires=[
        "yoti>=2.10.0"
        "cryptography>=2.8.0",
        "python-dotenv>=0.12.0"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="yoti sdk 2FA multifactor authentication verification identity login register verify 2Factor",
)
