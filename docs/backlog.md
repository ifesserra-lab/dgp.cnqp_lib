# General Project Backlog

**Central Tracking for Releases and Work Items**

## 1. Releases Log
Tracks the delivery of versions to production (Main Branch).

| Version | Date | Status | Description | PR / Commit |
|---------|------|--------|-------------|-------------|
| **v0.3.0** | 2026-01-07 | Released | ResearcherID & Granular Strategy Pattern | PR #13 |
| **v0.2.0** | 2026-01-09 | Released | Output Path Feature & Documentation Updates | [PR #12](https://github.com/ifesserra-lab/dgp.cnqp_lib/pull/12) |
| **v0.1.0** | 2026-01-09 | Released | OO Architecture Refactor & Modernization | [PR #3](https://github.com/ifesserra-lab/dgp.cnqp_lib/pull/3) / [4dadb7a](https://github.com/ifesserra-lab/dgp.cnqp_lib/commit/4dadb7a14776411a00ff8e2968fd2a0cb47e69db) |
| **v0.0.0** | 2026-01-01 | Released | Project Initiation | - |

## 2. In Progress Items (Current Sprint)
Reflecting active work from `SI.3 Product Backlog`.

- **CNPq Crawler Library**
    - [x] Issue #1 [Update Documentation and Implement Test Suite](https://github.com/ifesserra-lab/dgp.cnqp_lib/issues/1) ([PR #3](https://github.com/ifesserra-lab/dgp.cnqp_lib/pull/3) - Merged)
    - [x] Issue #2 [Modernize project structure with pyproject.toml](https://github.com/ifesserra-lab/dgp.cnqp_lib/issues/2) ([PR #3](https://github.com/ifesserra-lab/dgp.cnqp_lib/pull/3) - Merged)

- **Epic 3: Dados de Execução FAPES (Release 3)**
    - [ ] US-006 [Extração de Editais FAPES (PDF)](https://github.com/ifesserra-lab/horizon_etl/issues/1)

## 3. Hierarchical Status
Mapping Epics -> User Stories -> Tasks status.

### CNPq Crawler Library
- **Issue #1**: Done (Merged via PR #3)
- **Issue #2**: Done (Merged via PR #3)

### R3 - SigFapes
- **US-006**: Ready
    - T-006 [Dev] Scraper: Pending
    - T-007 [Dev] Parser: Pending
    - T-008 [Dev] Matcher: Pending
    - T-009 [Ops] Flow: Pending
