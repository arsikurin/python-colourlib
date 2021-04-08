import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colourlib",
    version="0.3.0",
    author="arsikurin",
    description="Python terminal colour library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    py_modules=["colourlib"],
    package_dir={"": "colourlib/src"},
)
