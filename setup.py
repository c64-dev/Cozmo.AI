import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CozmoAI", 
    version="0.4.9",
    author="c64-dev",
    author_email="nikosl@protonmail.com",
    description="Adding AI chat and voice command functionality to Cozmo robot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c64-dev/Cozmo.AI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
