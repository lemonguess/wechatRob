from setuptools import setup, find_packages
import pathlib
import re

WORK_DIR = pathlib.Path(__file__).parent

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = ""
exec(open('CuteCat/__version__.py').read())


setup(
    name="python-CuteCat-iHttp",
    version=__version__,
    description='Framework for WeChat hooks',
    author='honus',
    author_email="",
    url="",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires='>=3.7',
    keywords=["python-CuteCat-iHttp", ],
    install_requires=[
        "flask",
        "requests",
        "python-magic",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent"
    ]
)
