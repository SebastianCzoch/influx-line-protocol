import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


setuptools.setup(
    name='influx-line-protocol',
    description='Implementation of influxdata line protocol format in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.4',
    url='https://github.com/SebastianCzoch/influx-line-protocol',
    author='Sebastian Czoch',
    author_email='sebastian@czoch.pl',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    setup_requires=[
        "flake8"
    ]
)
