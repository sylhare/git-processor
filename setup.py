from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    requirements = file.read().split("\n")

with open('dev-requirements.txt') as file:
    dev_requirements = file.read().split("\n")

setup(
    name='Git Processor',
    version='0.1',
    description='Process and parse through git log statistic',
    long_description = long_description,
    keywords='git processor data science',
    url='https://github.com/sylhare/git-processor',
    author='sylhare',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib'],
    tests_require=['tox', 'pytest', 'pylint'],
)
