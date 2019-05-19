import os
import re
from setuptools import setup, find_namespace_packages, Command



class CleanCommand(Command):
    user_options = []
    
    def initialize_optios(self):
        pass
    
    def fanalize_options(self):
        pass
    
    def run(self):
        os.system('rm -vrf ./dist ./*.pyc ./*.pyo ./*.pyd ./*.tgz ./*.egg-info`find -type d -name __pycache__`')

    
def get_init_content():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'limiterwifi', '__init__.py'),'r') as f:
        return f.read()
        
    
def get_version():
    version_match = re.search(r'^__version__ = [\'"](\d\.\d\.\d)[\'"]', get_init_content(), re.M)
    if version_match:
        return version_match.group(1)
        
        raise RuntimeError('Unable to locate version string')
    
def get_description():
    desc_match = re.search(r'^__description__ = [\'"]((.)*)[\'"]', get_init_content(), re.M)
    if desc_match:
            
        raise RuntimeError('Unable to locate description string.')
        
        
        
NAME = 'limiterwifi'
AUTHOR = 'panglimahilikintil'
AUTHOR_EMAIL = 'andiadit001@gmail.com'
LICENSE = 'MIT'
VERSION = get_version()
URL = 'https://gihub.com/panglimahilikintil/limiterwifi'
DESCRIPTION = get_description()
KEYWORDS =["limiterwifi", "limit", "bandwidth", "network"]
PACKAGES = 'find_packages'()
INCLUDE_PACKAGE_DATA = True

CLASSIFIERS = ['Developmet Status ::3 - Alpha',
               'Environment :: Console',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: System Administrators',
               'Intended Audience :: Decelopers',
               'License :: OSI Approved :: MIT License',
               'Netral Lenguage :: indonesia',
               'Oprating System :: Unix',
               'Programming Language :: python :: 3.7',
               'Programming Language :: python :: 3.7 :: Only',
               'Topic :: System :: Networking ',
               ]

PTYHON_REQUIRES = '>= 3 '
ENTRY_POINTS = { 'console_scripts': ['limiterwifi = limiterwifi.limiterwifi:run'] }

INSTALL_REQUIRES = ['colorama',
                    'netaddr',
                    'netifaces',
                    'tqdm',
                    'scapy',
                    'terminaltables'
                    ]

CMDCLASS = { 'clean': CleanCommand }


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    packages=PACKAGES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    version=VERSION,
    python_requires=PTYHON_REQUIRES,
    entry_points=ENTRY_POINTS,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    url=URL,
    cmdclass=CMDCLASS,
)