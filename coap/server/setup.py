import os
from setuptools import setup, find_packages

setup(
    name="server",
    version="0.0.1",
    author="Yassir Sennoun",
    author_email="ysennoun@xebia.fr",
    description=("An application to consume IoT data"),
    license="BSD",
    keywords="IoT, Mqtt, Coap, Elasticsearch",
    url="https://github.com/ysennoun/",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    python_requires='>=3.7',
)