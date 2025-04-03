from setuptools import setup

# Parse README.md as long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Parse requirements.txt as install_requires
with open("requirements.txt", "r", encoding="utf-8") as f:
    require = f.read().splitlines()

setup(
    name="portfolio_optimizer",  # Name of the package
    version="0.0",
    description="naive Markovicz model",
    author="Sziklai Dominik, Gátmezei Kornél",
    author_email="...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SirArthur100/scientific_python",
    project_urls={
        "Bug Tracker": "https://github.com/SirArthur100/scientific_python/issues",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=["src"],  # Name of the package directory
    install_requires=[require],
    python_requires=">=3.10",
)
