from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='slack-url-utils',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package of URL utilities for use in slack using a slash command',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['slack', 'url', 'utilities'],
    url='https://github.com/MSAdministrator/slack-url-utils',
    author='Josh Rickard'
)