from setuptools import setup
setup(
    name='smartruck-cli',
    version='0.0.1',
    packages=['pycli'],
    entry_point={
        'console_scripts': [
            'smartruck-cli = main.__main__:main'
        ]
    }
)