from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Christopher Kevin Costa",
    author_email="christopherkevin78@gmail.com",
    description="Image processing library made as a project challenge for Dio's Data Engineering bootcamp.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
