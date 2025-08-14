from setuptools import setup, find_packages
from pathlib import Path

# Read README.md with UTF-8 encoding
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="toast_animation",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        'flet',
    ],
    author="Heckerdev",
    author_email="simplelogin-newsletter.unwilling149@simplelogin.com",
    description="A package for creating animated toast notifications in Flet applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/louisdev12/flet_toasty.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
