from setuptools import find_packages,setup
from typing import List

REQ_END = "-e ."

def get_requirements(filePath:str)->List[str]:
    '''
    this fun will return the list of requirements
    '''
    requirements = []
    with open(filePath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [temp.replace("\n","") for temp in requirements ]

        if REQ_END in requirements:
            requirements.remove(REQ_END)
    return requirements

setup(
name='basicmlproject',
version='0.0.1',
author='COMA',
author_email='mahmoudqotb912@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)