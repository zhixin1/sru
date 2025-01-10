from setuptools import setup
import os
import codecs
import sys

PACKAGE = 'sru'


def readme():
    """ Return the README text.
    """
    with codecs.open('README.md', encoding='utf-8') as fh:
        return fh.read()


def get_version():
    """ Gets the current version of the package.
    """
    version_py = os.path.join(os.path.dirname(__file__), 'sru/version.py')
    with open(version_py) as fh:
        for line in fh:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip() \
                    .replace('"', '').replace("'", '')
    raise ValueError('Failed to parse version from: {}'.format(version_py))


def get_requirements():
    required = ['torch>=1.9.0']
    
    # Only add ninja as a requirement if not installed via conda
    try:
        import ninja
    except ImportError:
        if 'conda' not in sys.version:  # Check if running in conda environment
            required.append('ninja')
    
    return required


setup(
    # Package information
    name=PACKAGE,
    version=get_version(),
    description='Simple Recurrent Units for Highly Parallelizable Recurrence',
    long_description=readme(),
    long_description_content_type="text/markdown",  # make pypi render long description as markdown
    keywords='deep learning rnn lstm cudnn sru fast pytorch torch',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: PyTorch :: 1.9',
        'Framework :: PyTorch :: 2.0',
        'Framework :: PyTorch :: 2.1',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
    ],

    # Author information
    url='https://github.com/taolei87/sru',
    author='Tao Lei, Yu Zhang, Sida I. Wang, Hui Dai and Yoav Artzi',
    author_email='tao@asapp.com',
    license='MIT',

    # What is packaged here.
    packages=['sru', 'sru/csrc'],

    # What to include
    package_data={
        '': ['*.txt', '*.rst', '*.md', '*.cpp', '*.cu']
    },

    # Dependencies
    install_requires=get_requirements(),
    python_requires='>=3.7',
    zip_safe=False
)
