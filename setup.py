from setuptools import setup, find_packages

setup( 
    name='mypackage', 
    version='0,1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description='EDSA Example Python Code',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RogerA11',
    author='Roger Arendse',
    author_email='roger.arendse713@gmail.com'
) 