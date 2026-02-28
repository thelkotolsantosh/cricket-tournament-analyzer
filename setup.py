from setuptools import setup, find_packages

setup(
    name="cricket-tournament-analyzer",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "tabulate",
        "matplotlib",
        "rich"
    ],
    author="thelkotolsantosh",
    description="Cricket Tournament Analytics and NRR Simulator",
)
