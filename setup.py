from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='git_processor',
    version='0.4',
    description='Process and parse through git log statistic',
    long_description=str(long_description),
    keywords='git git_processor data science',
    url='https://github.com/sylhare/git-git_processor',
    author='sylhare',
    author_email='sylhare@outlook.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['git_processor'],
    install_requires=['pandas', 'matplotlib'],
)
