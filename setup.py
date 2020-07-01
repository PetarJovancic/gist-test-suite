from setuptools import setup

setup(
    name='gist_test_suite',
    version='1.0',
    packages=['gist_test_suite'],
    url='https://github.com/PicnicNext/picnic-qa-PetarJovancic',
    license='',
    author='Petar Jovancic',
    author_email='petarjovancic93@gmail.com',
    description='Test automation suite for GitHub/Gist',
    install_requires=['pip','pytest','jsonpath','pytest-html'],
)