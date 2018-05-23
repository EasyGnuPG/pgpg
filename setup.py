from setuptools import setup, find_packages


def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except (FileNotFoundError, IOError):
        pass


setup(
    name='pgpg',
    version='0.1.0a1',
    url='https://github.com/EasyGnuPG/pgpg',
    author='Divesh Uttamchandani',
    author_email='diveshuttamchandani@gmail.com',
    license='GPLv3',
    description='An easy to use wrapper for GnuPG',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='gpg gpg2 pgpg egpg',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Education',

        'Topic :: Security :: Cryptography',

        'License :: OSI Approved :: GNU Affero General Public License v3'

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],

    project_urls={
            'Documentation': 'https://github.com/EasyGnuPG/pgpg/',
            'Source': 'https://github.com/EasyGnuPG/pgpg/',
            'Tracker': 'https://github.com/EasyGnuPG/issues',
    },

    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'pgpg=pgpg.cli:main'
        ],
    }
)
