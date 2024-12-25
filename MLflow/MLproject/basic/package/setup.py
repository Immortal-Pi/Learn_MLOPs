from setuptools import setup

setup(
    name='package',
    version='0.1',
    description='A useful package',
    author='T Amruth Pai',
    author_email='amruthpaiuni@gmail.com',
    packages=['package.feature','package.ml_training'], # storing code 
    install_requires=['numpy','pandas','scikit-learn','matplotlib','mlflow']
)