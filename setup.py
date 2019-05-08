from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='spacemenu',
    version='0.1',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/spacemenu',
    description='A spacemacs inspired gtk library',
    long_description=readme(),
    license='GPLv3+',
    packages=find_packages(exclude=('test')),
    include_package_data=True,
    install_requires=['pycairo','PyGObject'],
    # TODO: remove entry point
    entry_points={
        'console_scripts': ['spacemenu=spacemenu.test:main']
    }
)

