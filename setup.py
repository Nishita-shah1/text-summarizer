from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the specified file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to remove newline and whitespace

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='text-summarizer',
    version='0.0.1',
    author='Nishita',
    author_email='nishita182005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A small package for summarizing text',
    long_description=open('README.md').read(),  # Ensure README is properly included
    long_description_content_type='text/markdown',  # Specify the format of long_description
    url='https://github.com/Nishita-shah1/text-summarizer',  # Replace with your actual repo URL
    classifiers=[
        'Programming Language :: Python :: 3.8',  # Update as per your Python version
        'License :: OSI Approved :: MIT License',  # Example classifier, update as necessary
        'Operating System :: OS Independent',
    ],
)
