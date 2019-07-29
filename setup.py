#!/usr/bin/env python3

"""Setup script"""

from setuptools import setup

setup(
    name="neutron-dnscurrent-plugin",
    description="Use dns_current_name as machine hostname",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Unipart Digital",
    author_email="sysadmins@unipart.io",
    url="https://github.com/unipartdigital/neutron-dnscurrent-plugin",
    license="Apache",
    version="0.0.2",
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
    packages=[
        'neutron_dnscurrent',
    ],
    install_requires=[
        'neutron',
    ],
    entry_points={
        'neutron.ml2.extension_drivers': [
            'dnscurrent=neutron_dnscurrent:DNSCurrentExtensionDriver',
        ],
    },
)
