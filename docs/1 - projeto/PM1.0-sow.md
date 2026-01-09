# Statement of Work (SOW)
**Projeto:** dgp.cnqp_lib
**Data:** 09/01/2026
**Autor:** Antigravity (Senior PM)
**Versão:** 2.0

---

# 1. Introdução
## 1.1 Propósito
Este documento define o escopo, objetivos e entregáveis da biblioteca **dgp.cnqp_lib**. A biblioteca visa extrair dados estruturados do Espelho de Grupos de Pesquisa do CNPq e disponibilizá-los em formato JSON para integração com outros sistemas.

## 1.2 Justificativa
Sistemas institucionais de pesquisa e extensão frequentemente necessitam de dados do CNPq (líderes, linhas de pesquisa, recursos humanos) para complementar suas bases. A biblioteca **dgp.cnqp_lib** fornece uma solução reutilizável e robusta para essa extração.

Esta biblioteca é necessária para:
- **Integração de Dados**: Permitir que outros sistemas enriqueçam suas bases com informações do CNPq.
- **Reusabilidade**: Prover uma dependência Python que pode ser consumida por múltiplos projetos ETL.
- **Manutenibilidade**: Centralizar a lógica de extração do CNPq em um único pacote OO.

---

# 2. Escopo do Projeto

## 2.1 O que ESTÁ no Escopo (In-Scope)
- **Extração de Dados do CNPq**:
    - Nome do Grupo de Pesquisa.
    - Líderes do grupo.
    - Linhas de pesquisa.
    - Recursos Humanos (Estudantes, Pesquisadores).
- **Saída JSON**:
    - Arquivo JSON nomeado dinamicamente após o grupo.
- **Arquitetura OO**:
    - Classes (`CnpqCrawler`, `FieldsetParser`, `TableExtractor`).

## 2.2 O que NÃO ESTÁ no Escopo (Out-Scope)
- Persistência em banco de dados (responsabilidade do consumidor).
- Orquestração de múltiplas fontes (Lattes, FAPES, etc.).
- Dashboards ou visualizações.
- Análises ou transformações complexas além da extração estruturada.

---

# 3. Objetivos de Negócio
1.  **Biblioteca Reutilizável**: Ser consumida por projetos ETL maiores (ex: Horizon ETL).
2.  **Dados Estruturados**: Fornecer JSON limpo e normalizado do CNPq.
3.  **Facilitar Integração**: Reduzir fricção para outros sistemas que necessitam de dados do CNPq.

---

# 4. Stakeholders
- **Desenvolvedores de ETL**: Que consomem a biblioteca em pipelines Prefect/Airflow.
- **Sistemas Institucionais**: Que precisam complementar dados de grupos de pesquisa.

---

# 5. Premissas e Restrições
## 5.1 Premissas Técnicas
- **Linguagem**: Python 3.8+.
- **Navegação**: Playwright (para renderização de JavaScript).
- **Arquitetura**: Orientação a Objetos (OO).

## 5.2 Restrições
- A biblioteca não controla rate limits (responsabilidade do consumidor).
- Mudanças no layout do site CNPq podem quebrar a extração.
