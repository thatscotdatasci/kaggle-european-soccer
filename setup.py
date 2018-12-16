try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('packages.dat') as f:
    packages = f.readlines()
packages = [s.strip() for s in packages]


setup(
    name='kaggleEuroSoc',
    version=open('version.txt').read().strip(),
    packages=packages,
    description='Simple library created to migrate data from the Kaggle European Soccer data set (https://www.kaggle.com/hugomathien/soccer) SQLite database to a PostgreSQL database',
    author='Alan Clark',
    author_email='alan@thatscotdatasci.com',
    url='thatscotdatasci.com',
    platforms='linux, windows',
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read()
)
