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
        
    
