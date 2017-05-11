import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-markdown-filter',
    version='0.0.1',
    packages=['markdown_filter'],
    include_package_data=True,
    license='MIT',
    description='Markdown template filter for Django.',
    long_description=README,
    url='https://github.com/mrtc0/django-markdown-filter',
    author='mrtc0',
    author_email='mrtc0.py@gmail.com',
    classifiers=[
        'Framework :: Django',
    ],
    install_requires=[
        'django',
        'markdown2',
        'bleach',
    ],
)
