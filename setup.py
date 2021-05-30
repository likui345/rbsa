from distutils.core import setup
setup(
    name='rbsa',
    version='v0.1',
    py_modules=['rbsa.RBSA'],
    author = 'likui',
    author_email = 'likui345@126.com',
    description = 'Reference genome based scaffolds anchoring',
    requires = ['os','string','collections','argparse']
)
