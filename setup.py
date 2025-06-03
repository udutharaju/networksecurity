# setup.py contains all general info about the versions and all
#tools
from setuptools import find_packages,setup
##find_package searches for packages in app that where__init__.py is found that is considered as a package
from typing import List


def get_requirements()->list[str]:
    '''
    this function will return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list



setup(
    name = "Networksecurity",
    version="0.0.1",
    author = "raju",
    author_email="rajuudutha9963@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
   

   
