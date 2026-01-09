# Product Backlog – Sprints
**Projeto:** dgp.cnqp_lib
**Responsável (PO):** Antigravity

---

# 1. Visão Geral
Este documento mapeia as User Stories do backlog principal para as sprints de desenvolvimento.

---

# 2. Release v0.0.1 (Fundação) - Sprint 0
**Status:** ✅ Concluído

### US-001 – Extração Básica
- T-001: Setup do ambiente Python.
- T-002: Implementação de script standalone com Playwright.
- T-003: Validação de extração de título e tabelas.

---

# 3. Release v0.1.0 (Modernização & OO) - Sprint 1-3
**Status:** ✅ Concluído

### US-002 – Modernização de Estrutura
- [x] S1: Refatoração para Classes Base (`BaseExtractor`).
- [x] S2: Implementação de CLI e `pyproject.toml`.
- [x] S3: Testes Unitários e CI/CD Github Actions.

---

# 4. Release v0.2.0 (Performance) - Backlog Futuro
**Status:** 📋 Planejado

### US-003 – Tratamento de Erros
- Implementar RetryDecorator.
- Tratar TimeoutException do Playwright.

### US-004 – Logging Estruturado
- Configurar Loguru.
- Padronizar logs JSON.
