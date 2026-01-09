# SI1 - Requisitos do Sistema

## 1. Introdução
Este documento define os requisitos para a biblioteca de extração de dados do Espelho de Grupos de Pesquisa do CNPq (`dgp_cnpq_lib`).

## 2. Requisitos Funcionais

### RF-01: Extração de Dados de Grupo
- **Descrição**: O sistema deve extrair dados estruturados de uma página pública do Espelho de Grupo de Pesquisa.
- **Entrada**: URL da página do grupo.
- **Saída**: Dicionário de dados ou Arquivo JSON.

### RF-02: Saída JSON Padronizada
- **Descrição**: O sistema deve salvar os dados extraídos em um arquivo JSON.
- **Regra**: O nome do arquivo deve ser baseado no nome do grupo (ex: `grupo_x.json`).

### RF-03: Extração de Metadados
- **Descrição**: O sistema deve identificar e extrair:
    - Nome do Grupo.
    - Líderes.
    - Linhas de Pesquisa.
    - Recursos Humanos (Estudantes, Pesquisadores).

## 3. Requisitos Não Funcionais

### RNF-01: Dependências
- **Descrição**: O sistema deve utilizar `playwright` para navegação e renderização de JavaScript.

### RNF-02: Arquitetura
- **Descrição**: O sistema deve seguir o paradigma Orientado a Objetos (OO).
