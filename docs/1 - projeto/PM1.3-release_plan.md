# Release Plan
**Projeto:** dgp_cnpq_lib
**Versão:** 2.0
**Última Atualização:** 09/01/2026

---

# 1. Visão Geral de Releases
O projeto segue o modelo de releases incrementais baseadas em funcionalidades.

| Release | Objetivo Principal | Data | Status |
|---------|-------------------|------|--------|
| **v0.1.0** | OO Architecture & Modernization | 09/01/2026 | ✅ Released |
| **v0.2.0** | Performance & Error Handling | Q1 2026 | 📋 Planejado |
| **v1.0.0** | Production Stable | Q2 2026 | 📋 Planejado |

---

# 2. Detalhamento por Release

## 2.1 Release v0.1.0 – OO Architecture & Modernization ✅
**Data de Release:** 09/01/2026  
**Status:** Released to Production (main)

**Objetivos Alcançados:**
- ✅ Refatoração completa para arquitetura OO
- ✅ Migração para `pyproject.toml` (padrão moderno)
- ✅ CI/CD com linting automatizado
- ✅ Suite de testes (6 testes unitários/integração)
- ✅ Documentação completa atualizada

**Funcionalidades Implementadas:**
- **Classes OO**:
  - `BaseExtractor`: Utilitários base para extração
  - `TableExtractor`: Parsing de tabelas HTML
  - `FieldsetParser`: Parsing de fieldsets CNPq
  - `CnpqCrawler`: Orquestração com Playwright
- **CLI Entry Point**: `python -m dgp_cnpq_lib <url>`
- **Modernização**:
  - `pyproject.toml` com hatchling
  - `requirements.txt` e `requirements-dev.txt`
  - Linting (black, isort, flake8)

**PRs e Issues:**
- PR #3: Feature implementation
- PR #4: Release to master
- Issue #1: Documentation and Test Suite
- Issue #2: Modernize Project Structure

**Commit SHA:** `2c91747`

---

## 2.2 Release v0.2.0 – Performance & Error Handling 📋
**Data Estimada:** Q1 2026  
**Status:** Planejado

**Objetivos:**
- Otimização de performance para extração em lote
- Tratamento robusto de erros e timeouts
- Retry logic com backoff exponencial
- Logging estruturado (JSON)

**Funcionalidades Planejadas:**
- Sistema de cache para páginas já extraídas
- Parallel extraction com asyncio
- Graceful degradation para páginas malformadas
- Métricas de performance (Prometheus-compatible)

---

## 2.3 Release v1.0.0 – Production Stable 📋
**Data Estimada:** Q2 2026  
**Status:** Planejado

**Objetivos:**
- Estabilidade comprovada em produção
- Cobertura de testes > 90%
- Documentação completa para desenvolvedores
- Exemplo de integração com outros sistemas

**Funcionalidades Planejadas:**
- Plugin system para extensibilidade
- Export adicional (CSV, Excel)
- API HTTP (opcional) para integração remota
- Containerização (Docker)

---

# 3. Estratégia de Versionamento (SemVer)

Seguimos **Semantic Versioning** (SemVer 2.0.0):
- **MAJOR** (X.0.0): Breaking changes incompatíveis
- **MINOR** (0.X.0): Novas funcionalidades retro-compatíveis
- **PATCH** (0.0.X): Bug fixes retro-compatíveis

**Tags Git:**
- Cada release **DEVE** ter uma tag `vX.Y.Z`
- Tag `latest` sempre aponta para a release mais recente
- Tags são criadas automaticamente no merge para `main`

---

# 4. Processo de Release (GitFlow)

1. **Development**: Features desenvolvidas em branches `feat/*` → merge para `developing`
2. **Quality Gate**: CI/CD valida testes e linting em `developing`
3. **Release PR**: `developing` → `main` (título: `release: vX.Y.Z`)
4. **Tag**: Após merge, criar tag `git tag vX.Y.Z && git push origin vX.Y.Z`
5. **GitHub Release**: CI/CD cria release automaticamente com assets compilados
6. **Publish**: Pacote publicado no GitHub Packages

---

# 5. Milestones no GitHub

Cada release major/minor **DEVE** ter um Milestone correspondente:
- ✅ `v0.1.0 - OO Architecture` (Fechado: 09/01/2026)
- 📋 `v0.2.0 - Performance` (A criar)
- 📋 `v1.0.0 - Stable` (A criar)
