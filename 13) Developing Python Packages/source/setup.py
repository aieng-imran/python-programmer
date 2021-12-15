from setuptools import setup

setup(
   name = 'helloworld',
   version='0.0.1',
   setup_requires=['wheel'],
   description='Say hello!',
   py_modules=["helloworld"],
   package_dir={'','source'}
    )