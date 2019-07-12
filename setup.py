import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipfinder-io",
    version="1.0.0",
    description="Official Python library for IPFinder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ipfinder-io/ip-finder-python",
    author="IPFinder",
    author_email="mohamed@ipfinder.io",
    license="Apache License 2.0",
    # packages=["ipfinder", "ipfinder.Validation", "ipfinder.Exception"],
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
