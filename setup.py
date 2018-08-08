"""For pip."""
from setuptools import find_packages, setup

exec(open("fonduer/_version.py").read())
setup(
    name="fonduer",
    version=__version__,
    description="Knowledge base construction system for richly formatted data.",
    long_description=open("README.rst").read(),
    packages=find_packages(),
    install_requires=[
        "bs4",
        "editdistance",
        "lxml==3.6.4",
        "nltk",
        "numba",
        "numbskull",
        "numpy>=1.11",
        "pandas",
        "psycopg2-binary",
        "scipy>=0.18",
        "spacy>=2.0.7",
        "sqlalchemy>=1.0.14",
        "tensorflow>=1.0",
        "treedlib",
        "wand",
    ],
    keywords=["fonduer", "knowledge base construction", "richly formatted data"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest>=3.4.0", "flake8"],
    include_package_data=True,
    url="https://github.com/HazyResearch/fonduer",
    classifiers=[  # https://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Tracker": "https://github.com/HazyResearch/fonduer/issues",
        "Source": "https://github.com/HazyResearch/fonduer",
    },
    python_requires=">=3.6",
    author="Hazy Research",
    author_email="senwu@cs.stanford.edu",
    license="MIT",
)
