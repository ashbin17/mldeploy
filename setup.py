"""A setuptools based setup module"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name='mldeploy',  # Required
    version='0.1.0',  # Required
    description='A sample ml flask app.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/gauthamp10/mldeploy',  # Optional
    author='Guatham Prakash',  # Optional
    author_email='gauthamp10',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students',
        'Topic :: Machine Learning :: Data Science',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='ml, flask app, machine learning, deployment',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    install_requires=[
        'flask',
        'gunicorn',
	'pandas',
	'scikit-learn'
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    python_requires='=3.6.9',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/gauthamp10/mldeploy/issues',
        'Source': 'https://github.com/gauthamp10/mldeploy',
    },
)
