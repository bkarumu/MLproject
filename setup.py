# Building the application as a package itself
from setuptools  import find_packages,setup
from typing import List
# this setup is the metadata version of my project"
# '-e.' in the requirements fle is to rigger the setup file,
# but not to run while i initiate the library.
# So the first step is creat a variable for -e.
HYPHEN_E_DOT = '-e.'

def get_requirements (file_path:str) -> List[str]:
    '''This function will return list of requirmemts'''
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace ("\n"," ")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements
                                
setup(
name = 'mlproject',
version='0.0.1',
author = 'bhavika',
author_email= 'bhavikareddy.karumuri@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt') # this function will pick all the libraries listed in requirements.txt file
)
