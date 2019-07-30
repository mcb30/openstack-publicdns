#!/usr/bin/env python3

"""Setup script"""

from setuptools import setup, find_packages

setup(
    name="openstack-publicdns",
    description="OpenStack public DNS plugins",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Unipart Digital",
    author_email="sysadmins@unipart.io",
    url="https://github.com/unipartdigital/openstack-publicdns",
    license="Apache",
    version="0.0.4",
    classifiers=[
        "Environment :: OpenStack",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=[
        'neutron',
    ],
    entry_points={
        'neutron.ml2.extension_drivers': [
            'publicdns=openstack_publicdns:PublicDNSExtensionDriver',
        ],
    },
)
