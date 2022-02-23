from setuptools import setup, find_packages

setup(
    name='wordle',
    version='0.0.2',
    install_requires=[
        'selenium',
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "wordleRun=wordle.main:main"
        ]
    }
)