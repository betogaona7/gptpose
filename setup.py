from setuptools import setup, find_packages

setup(
    name="gptpose",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gptpose=gptpose.cli:main',
        ],
    },
    include_package_data=True
)