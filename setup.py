from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, 'eospyabi', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name='eospyabi',
    version=os.getenv('BUILD_VERSION', about['__version__']),
    description='Python library for the eos.io REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='deck',
    author_email='deck@eosnewyork.io',
    url='https://github.com/MajicGit/eospyABI',
    packages=find_packages(),
    test_suite='nose.collector',
    install_requires=[
        'requests',
        'base58>=1.0.3',
        'ecdsa',
        'colander',
        'pytz',
        'six',
        'pyyaml',
        'antelopy'
    ],
    entry_points={
        'console_scripts': [
            'validate_chain = eospyabi.command_line:validate_chain',
            'pycleos = eospyabi.command_line:cleos',
            'pytesteos = eospyabi.command_line:testeos',
        ],
    })
