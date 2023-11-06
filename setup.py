from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dev_portfolio/__init__.py
from dev_portfolio import __version__ as version

setup(
	name="dev_portfolio",
	version=version,
	description="This app helps in tracking, monitoring the day to day changes and in-depth reporting",
	author="Panigrahis.com",
	author_email="support@panigrahis.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
