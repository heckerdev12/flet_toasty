from setuptools import setup, find_packages

setup(
    name="toast_animation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flet',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for creating animated toast notifications in Flet applications.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/toast_animation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
