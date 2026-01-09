# DEPRECATED: This file is kept for backward compatibility only.
# Please use pyproject.toml for all package configuration.
# Install with: pip install -e .

from setuptools import find_packages, setup

setup(
    name="dgp_cnpq_lib",
    version="0.1.0",
    description="Biblioteca Python para extração de dados do Espelho de Grupos de Pesquisa do CNPq",
    author="PaulosJunior",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "playwright",
    ],
    python_requires=">=3.8",
)
