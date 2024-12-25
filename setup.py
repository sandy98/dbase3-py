from setuptools import setup, find_packages

setup(
    name='dbase-iii',
    version='0.1.0',
    description='A Python library to manipulate DBase III database files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/yourusername/dbase-iii-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)