# SI1 - Requisitos do Sistema
**Projeto:** dgp.cnqp_lib
**Versão:** v0.1.0
**Tipo:** Biblioteca Python

---

# 1. Introdução
Este documento define os requisitos técnicos e funcionais para a biblioteca `dgp_cnpq_lib`, responsável pela extração automatizada de dados públicos do Espelho de Grupo de Pesquisa do CNPq.

---

# 2. Requisitos Funcionais (RF)

### RF-01: Extração de Dados Completos
- **Descrição**: O sistema deve extrair todos os dados visíveis nos fieldsets da página do grupo.
- **Entrada**: URL pública do espelho (ex: `dgp.cnpq.br/espelhogrupo/...`).
- **Saída**: Dicionário aninhado contendo:
    - Identificação e Liderança.
    - Áreas de especialidade.
    - Recursos Humanos (Estudantes, Técnicos, Pesquisadores).
    - Linhas de Pesquisa.

### RF-02: Interface de Linha de Comando (CLI)
- **Descrição**: A biblioteca deve fornecer uma CLI executável via `python -m dgp_cnpq_lib <url>`.
- **Ação**: Ao executar, deve extrair os dados e salvar em disco.
- **Saída**: Feedback no `stdout` ("Navigating to...", "Data saved to...").

### RF-03: Persistência em JSON
- **Descrição**: Os dados extraídos devem ser salvos em arquivos JSON.
- **Formato**: Nome do arquivo deve ser sanitizado baseado no nome do grupo (ex: `grupo_de_pesquisa_em_ia.json`).

### RF-04: Parsing de Tabelas Dinâmicas
- **Descrição**: O sistema deve identificar tabelas HTML dentro dos fieldsets e convertê-las para listas de objetos JSON.
- **Detalhe**: Deve tratar colunas como chaves (normalizadas para `snake_case`) e linhas como valores.

---

# 3. Requisitos Não Funcionais (RNF)

### RNF-01: Stack Tecnológica
- **Linguagem**: Python 3.8+
- **Engine**: Playwright (para renderização de JS e navegação).
- **Packaging**: `hatchling` (backend de build).

### RNF-02: Arquitetura Orientada a Objetos
- **Padrão**: O código deve ser organizado em classes com responsabilidades únicas (`Extractor`, `Parser`, `Crawler`).
- **Extensibilidade**: Facilidade para adicionar novos tipos de extratores sem modificar o crawler principal.

### RNF-03: Qualidade de Código
- **Linting**: O código deve passar, sem erros, por:
    - `black` (formatação, line-length 100).
    - `flake8` (estilo).
    - `isort` (imports).
- **Testes**: Cobertura de testes unitários (`pytest`) para os parsers.
