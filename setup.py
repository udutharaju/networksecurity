# setup.py contains all general info about the versions and all

from setup import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_path.readlines()
        requirements=[req.replace('\n','') for req  in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = 'networksecurity'
    version = '0.0.1',
    author = 'raju',
    author_email = 'rajuudutha9963@gmail.com'
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

    
)

