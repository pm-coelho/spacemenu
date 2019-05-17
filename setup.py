from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='spacemenu',
    version='0.3',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/spacemenu',
    description='A spacemacs menu inspired gtk module',
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='GPLv3+',
    packages=find_packages(exclude=('test')),
    include_package_data=True,
    install_requires=['pycairo','PyGObject'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

