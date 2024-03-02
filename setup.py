import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "multi_service_utils",
    version = "0.0.1",
    author = "Harshal Patel",
    author_email = "harshalpatel12.py@gmail.com",
    description = "This package contains utility functions shared across multiple services in the application.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/harshll/",
    project_urls = {
        "Bug Tracker": "https://github.com/harshll/",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    install_requires = ['novu'],
    python_requires = ">=3.6"
)