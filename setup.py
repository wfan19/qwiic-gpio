from setuptools import find_packages, setup

setup(
    name='qwiic_gpio',
    packages=find_packages(),
    version='0.1.0',
    description='RPi.GPIO and Jetson.GPIO like api for qwiic''s GPIO expansion board',
    author='Bill Fan',
    license='MIT',
)