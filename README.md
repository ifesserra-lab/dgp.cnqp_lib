# DGP CNPq Lib

Uma biblioteca Python para extrair dados estruturados (JSON) de páginas de "Espelho de Grupo de Pesquisa" do CNPq.

Este projeto utiliza [Playwright](https://playwright.dev/) para navegar e extrair dados dinâmicos.

## Funcionalidades

- Extração completa de dados do grupo (Identificação, Endereço, Linhas de Pesquisa, RH, etc.)
- Tratamento automático de datas (início/fim)
- Saída em JSON normalizado e limpo

## Instalação

```bash
pip install .
# Ou instale as dependências manualmente
pip install playwright
playwright install chromium
```

## Como Usar

### Como Biblioteca

```python
from dgp_cnpq_lib.crawler import crawl_cnpq_group
import json

url = "http://dgp.cnpq.br/dgp/espelhogrupo/4201359100034312"
data = crawl_cnpq_group(url)

print(json.dumps(data, indent=2, ensure_ascii=False))
```

### Script Standalone

Você também pode rodar o módulo diretamente se estiver na raiz do projeto:

```bash
python -m src.dgp_cnpq_lib.crawler
```
(Certifique-se de ajustar o script para aceitar argumentos via linha de comando se desejar mais flexibilidade).

## Estrutura do Projeto

- `src/dgp_cnpq_lib`: Código fonte da biblioteca.
- `setup.py`: Configuração de instalação.

## Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request
