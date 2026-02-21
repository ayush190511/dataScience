from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

 

setup(
    name="dsProject",
    version="0.0.1",
    author="Ayush Mishra",
    author_email="ayushmishra642001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)