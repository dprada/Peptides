import distutils.extension
from setuptools import setup, find_packages

setup(
    name='peptides',
    version='0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'peptides': 'peptides'},
    packages=find_packages(),
    package_data={'peptides': []},
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/Peptides',
    license='MIT',
    description="doc to be written",
    long_description="long doc to be written",
)
