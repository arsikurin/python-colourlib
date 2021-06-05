import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="colourlib",
    version="0.5.3",
    author="arsikurin",
    description="Python terminal colour library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    py_modules=["colourlib"],
    package_dir={"": "colourlib/src"},
)
