from setuptools import setup, find_packages

required_packages = ['graphql-core>=0.4.9', 'werkzeug>=0.11.0']

setup(
    name='Werkzeug-GraphQL',
    version='0.1.0',
    description='Adds GraphQL support to your Werkzeug application',
#    long_description=open('README.rst').read(),
    url='https://github.com/graphql-python/flask-graphql',
    download_url='https://github.com/graphql-python/flask-graphql/releases',
    author='Kai Strempel',
    author_email='kstrempel@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='api graphql protocol rest flask',
    packages=find_packages(exclude=['tests']),
    install_requires=required_packages,
    tests_require=['pytest>=2.7.3'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
