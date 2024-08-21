from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(filepath:str)->list[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
        return requirements

setup(
    name="Food data",
    version="0.0.1",
    author="Robin Aluma",
    author_email="alumarobin@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)