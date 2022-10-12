from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Template_Pypi",
    version="0.0.1",
    author="Ender3245",
    author_email="Enderdragon3245@gmail.com",
    description="project for library",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Enderzin3245",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)