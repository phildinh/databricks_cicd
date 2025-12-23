from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.1.0",
    description="A Databricks project for Citibike ETL pipeline",
    author="pdinh",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    install_requires=["setuptools"]
)