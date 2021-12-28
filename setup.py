from setuptools import setup, find_packages

setup(
    name='gdrive-dataset',
    version='0.0.1',
    description='easy downloader for google drive datasets',
    author='teddylee777',
    author_email='teddylee777@gmail.com',
    url='https://github.com/teddylee777/datasets',
    install_requires=['googledrivedownloader'],
    packages=find_packages(exclude=[]),
    keywords=['dacon', 'teddylee777'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
