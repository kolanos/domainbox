import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='DomainBox',
    version='0.1',
    url='http://github.com/kolanos/domainbox',
    license='MIT',
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    description='A SOAP client for the DomainBox API.',
    long_description=read('README.rst'),
    py_modules=['domainbox'],
    platforms='any',
    install_requires=['suds'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
