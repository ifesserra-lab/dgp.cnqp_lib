from setuptools import setup, find_packages

setup(
    name="dgp_cnpq_lib",
    version="0.1.0",
    description="Uma biblioteca para extrair dados do Espelho de Grupo de Pesquisa do CNPq",
    author="PaulosJunior",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "playwright",
    ],
    python_requires=">=3.8",
)
