from setuptools import setup, find_packages
setup(
    name='rbsa',
    version= 0.1 ,
    packages = find_packages(),
    py_modules =['rbsa.RBSA'],
    author = 'likui',
    author_email = 'likui345@126.com',
    description = 'Reference genome based scaffolds anchoring',
)
