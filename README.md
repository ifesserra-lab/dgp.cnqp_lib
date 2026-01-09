# dgp_cnpq_lib

**Biblioteca Python para extração de dados do Espelho de Grupos de Pesquisa do CNPq.**

## 📖 Visão Geral
`dgp_cnpq_lib` é uma biblioteca utilitária que extrai dados estruturados de páginas do [Espelho de Grupos de Pesquisa do CNPq](http://dgp.cnpq.br/) e os retorna em formato JSON. Ideal para integração com sistemas ETL e bases de dados institucionais.

## 🚀 Instalação
```bash
pip install .
```

## 💻 Uso
```bash
python -m dgp_cnpq_lib http://dgp.cnpq.br/dgp/espelhogrupo/<id>
```

**Saída**: Arquivo JSON nomeado dinamicamente após o grupo (ex: `grupo_de_inteligencia_artificial.json`).

### 🐍 Uso via Python

Você pode utilizar a biblioteca diretamente em seu código Python:

```python
from dgp_cnpq_lib.core import CnpqCrawler

# 1. Instanciar o Crawler
crawler = CnpqCrawler()

# 2. Extrair dados de um Espelho de Grupo
url = "http://dgp.cnpq.br/dgp/espelhogrupo/0225175815967657"
data = crawler.get_data(url)

# 3. Utilizar os dados (dicionário)
print(f"Grupo: {data.get('nome_grupo')}")
print(f"Líderes: {data['lideres_do_grupo']}")
```

## 🏗️ Arquitetura
- **`core.py`**: `CnpqCrawler` - Orquestra a navegação (Playwright).
- **`extractors.py`**: Classes OO para parsing (BaseExtractor, TableExtractor, FieldsetParser).
- **`__main__.py`**: Interface CLI.

## 🧪 Testes
```bash
pytest tests/
```

## 📂 Documentação Completa
Veja [`docs/README.md`](docs/README.md) para a estrutura completa de governança e design.

## 📜 Licença
MIT
