from setuptools import setup, find_packages

setup(
    name='hmcalc',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='calculation packages',
    long_description=open('README.md').read(),
    url='https://github.com/Falconxx/python-library',
    author='Arkadiusz Sokolowski',
    author_email='230435@student.pwr.edu.pl'
)
