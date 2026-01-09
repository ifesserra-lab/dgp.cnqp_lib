# Product Backlog – dgp.cnqp_lib
**Responsável (PO):** Antigravity
**Versão:** v0.1.0

---

# 1. Visão Geral
Backlog focado no desenvolvimento da biblioteca de extração de dados do CNPq.

---

# 2. Epics & User Stories

## Epic 1: Fundação do Crawler (Release v0.0.1)
**Objetivo**: Estabelecer a capacidade básica de extrair dados via Playwright.

### US-001 – Extração Básica e CLI
- **Desc**: Criar script capaz de acessar URL e extrair JSON bruto.
- **Status**: ✅ Done (Refatorado na v0.1.0)

---

## Epic 2: Modernização e Arquitetura OO (Release v0.1.0)
**Objetivo**: Profissionalizar o código para padrões de mercado.

### US-002 – Modernização de Estrutura (Issue #2)
- **Desc**: Migrar para `pyproject.toml`, implementar OO, testes e CI.
- **Tasks**:
  - [x] Remover `setup.py`
  - [x] Criar Classes (`Core`, `Extractors`)
  - [x] Configurar GitHub Actions (Lint/Test)
- **Status**: ✅ Done (Released)

---

## Epic 3: Robustez e Performance (Release v0.2.0)
**Objetivo**: Garantir que o crawler funcione em escala e com resiliência.

### US-003 – Tratamento de Erros e Retries
- **Desc**: Implementar lógica de retry para timeouts e falhas de rede.
- **Prioridade**: Alta

### US-004 – Logging Estruturado
- **Desc**: Substituir prints por `logging` (JSON logs) para observabilidade.
- **Prioridade**: Média

---

# 3. Definition of Done (DoD)
- [ ] Código em Classes (OO)
- [ ] Testes Unitários Passando
- [ ] CI/CD Verde
- [ ] Documentação (`docs/`) Atualizada
