from setuptools import setup, find_packages

setup(
    name="icinga2",
    version="0.1a1",
    packages=find_packages(),
    author="Christoph Gebhardt",
    author_email="cg@zknt.org",
    description="Python client for Icinga2 REST API",
    license="GPL3",
    keywords="icinga2 rest api",
    url="https://github.com/hnrd/icinga2",
    install_requires=["requests",],
)
