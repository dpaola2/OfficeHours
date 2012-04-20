from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='officehours',
    version='0.0.1',
    description='A simple office hours scheduler',
    long_description=readme,
    author='Dave Paola',
    author_email='dpaola2@gmail.com',
    url='https://github.com/dpaola2/officehours',
    license=license,
    packages=find_packages(exclude=('tests'))
)

