from setuptools import setup, find_packages
from pip.req import parse_requirements
import re
import io
import os.path

here = os.path.abspath(os.path.dirname(__file__))

# get version from module source
version = None
version_re = re.compile(r"^__version__ = '(.*?)'$")
with open(os.path.join(here, 'genderize/__init__.py')) as f:
    for line in f:
        match = version_re.match(line)
        if match:
            version = match.group(1)
            break

# get requirements from Pip-style requirements.txt
install_requires = [str(req.req) for req
    in parse_requirements(os.path.join(here, 'requirements.txt'))]

# get long from README.rst
with io.open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='Genderize',
    version=version,
    description='Client for Genderize.io web service.',
    long_description=long_description,
    author='Jeremy Ehrhardt',
    author_email='jeremy@bat-country.us',
    url='https://github.com/SteelPangolin/genderize',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
