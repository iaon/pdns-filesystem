import os
from setuptools import setup

from pdns_filesystem import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pdns-filesystem',
      version=__version__,
      description='PowerDNS backend using file system',
      long_description=read('README.rst'),
      author='Ivan Onushkin',
      author_email='ivan.onushkin@gmail.com',
      license='Apache License 2.0',
      url='http://github.com/iaon/pdns-filesystem',
      packages=['pdns_filesystem'],
      scripts=['bin/pdns-filesystem'],
      tests_require=open('test-requirements.txt').readlines(),
      install_requires=open('requirements.txt').readlines(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Utilities'
        ]
     )
