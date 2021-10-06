import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="profile-python",
    version="0.0.4",
    author="João Lucas",
    author_email="joaolucasfp2001@gmail.com",
    description="Profile python is a script for you to view your data and github repositories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heroesofcode/profile-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'rich',
        'requests',
        'pyfiglet'
    ],
    project_urls={
        'Homepage': 'https://github.com/heroesofcode/profile-python',
    },
    entry_points={
        'console_scripts': [
            'profile-python=profile_python.__main__:main',
        ],
    },
)
