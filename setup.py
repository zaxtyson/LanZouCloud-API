import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lanzou-api",
    version="2.4.4",
    author="zaxtyson",
    author_email="zaxtyson@foxmail.com",
    description="LanZouCloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaxtyson/LanZouCloud-API",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
