# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-genericlabelinterpolator',
    version='1.1.0',
    author='Joël Schaerer',
    author_email='joelthelion@laposte.net',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKGenericLabelInterpolator',
    description=r'ITK classes for generic interpolation of label images.',
    long_description='itk-genericlabelinterpolator provides a generic '
                     'interpolator for label images to interpolate each '
                     'label with an ordinary image interpolator, and return '
                     'the label with the highest value.\n'
                     'Please refer to:\n'
                     'Schaerer J., Roche F., Belaroussi B., '
                     '"A generic interpolator for multi-label images.", '
                     'Insight Journal, January-December 2014, https://hdl.handle.net/10380/3506.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit Label-images Interpolation',
    url=r'https://github.com/InsightSoftwareConsortium/ITKGenericLabelInterpolator',
    install_requires=[
        r'itk>=5.2rc1'
    ]
    )
