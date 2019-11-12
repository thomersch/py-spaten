#!/usr/bin/env python

from setuptools import setup

test_deps = ['pytest', 'pytest-benchmark']
extras = {
  'test': test_deps
}

setup(name='spaten',
      version='0.4.1',
      description='Spaten File Format Library',
      author='Thomas Skowron',
      author_email='th@skowron.eu',
      url='https://github.com/thomersch/py-spaten',
      packages=['spaten'],
      install_requires=['Shapely', 'protobuf>=3.0.0'],
      test_requires=test_deps,
      extras_require=extras,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Topic :: Scientific/Engineering :: GIS"
      ])
