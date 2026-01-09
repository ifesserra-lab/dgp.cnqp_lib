# Product Backlog – Sprints Overview
**Projeto:** dgp.cnqp_lib
**Responsável (PO):** Antigravity
**Última Atualização:** 09/01/2026

---

# 1. Visão Geral
Este documento mapeia as User Stories do backlog principal para as sprints de desenvolvimento (Passadas e Futuras), servindo como histórico de execução e planejamento tático.

---

# 2. Histórico de Sprints

## Sprint 0: Fundação (Release v0.0.1)
**Período:** 01/01/2026 - 05/01/2026
**Status:** ✅ Concluído
**Entregas:**
- Setup do Repositório e Ambiente.
- Estrutura de Documentação (ISO 29110).
- Proof of Concept (PoC) do Crawler com Playwright.

## Sprint 1-3: Modernização & Release v0.1.0
**Período:** 06/01/2026 - 09/01/2026
**Status:** ✅ Concluído
**Entregas:**
- **US-001**: Extração Básica (Refatorada).
- **US-002**: Modernização de Estrutura.
    - Implementação de `BaseExtractor`, `TableExtractor`, `FieldsetParser`.
    - CLI `python -m dgp_cnpq_lib`.
    - Configuração de CI/CD (`ci.yml`, `release.yml`).
    - Migração para `pyproject.toml`.

---

# 3. Próximas Sprints (Planejamento)

## Sprint 4: Robustez (Release v0.2.0)
**Previsão:** Q1 2026
**Foco:** Performance e Tratamento de Erros.

### Backlog da Sprint
- **US-003**: Tratamento de Erros e Retries.
    - Implementar Decorators de Retry.
    - Tratamento específico de exceções do Playwright.
- **US-004**: Observabilidade.
    - Configurar Loguru com saída JSON.

## Sprint 5: Estabilidade (Release v1.0.0)
**Previsão:** Q2 2026
**Foco:** Preparação para Produção em Larga Escala.
