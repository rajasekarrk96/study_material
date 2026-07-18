from pathlib import Path
from setuptools import setup, find_packages

# Read the contents of README.md for the long description
long_description = Path("README.md").read_text()

setup(
    name="EduSphereDataStructure",
    version="1.0.0",  # Version represented as a string
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify the content type of long description
    packages=find_packages(exclude=["tests", "data"]),  # Using pathlib.Path for finding packages
)