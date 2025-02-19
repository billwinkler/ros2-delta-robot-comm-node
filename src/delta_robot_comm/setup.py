#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='delta_robot_comm',
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/delta_robot_comm']),
        ('share/delta_robot_comm', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bill Winkler',
    maintainer_email='bill.winkler@gmail.com',
    description='Delta robot communication node package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'delta_robot_comm_node = delta_robot_comm.delta_robot_comm_node:main'
        ],
    },
)
