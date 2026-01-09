# SDLC – dgp.cnqp_lib

Este repositório contém a biblioteca **dgp.cnqp_lib**, desenvolvida seguindo práticas ágeis e padrões de engenharia de software do **The Band Project**.

---

# 1. Visão Geral do Processo (SDLC)
O ciclo de vida de desenvolvimento segue o fluxo **Agile Standards**:

1.  **Iteração**: Sprints de 2 semanas (Cadência 1º e 15º do mês).
2.  **Branching**: GitFlow (`main`, `developing`, `feat/*`).
3.  **Versioning**: Semantic Versioning (vX.Y.Z).
4.  **Release**: Automatizada via GitHub Actions.

---

# 2. Estrutura de Documentação
A documentação é organizada conforme a **ISO 29110**:

### 1 - Projeto (Gerência)
- **PM1.0 SOW**: Statement of Work e Escopo.
- **PM1.3 Release Plan**: Planejamento de versões.
- **PM1.9 Status Reports**: Acompanhamento de progresso.

### 2 - Implementação (Engenharia)
- **SI.1 Requisitos**: Funcionais e Não-Funcionais.
- **SI.3 Design**: Arquitetura Técnica (OO).
- **SI.4 Construção**: Código Fonte (`src/`).
- **SI.5 Testes**: Suíte de Testes (`tests/`).

---

# 3. Padrões de Qualidade
Todo código submetido deve aderir a:
- **Style**: `black` (100 chars), `isort`, `flake8`.
- **Testing**: `pytest` (Cobertura mínima aceitável).
- **Design**: Orientação a Objetos (SOLID).
- **Review**: Pull Requests com CI passing obrigatório.

---

# 4. Links Úteis
- [Backlog Global](backlog.md)
- [Release Plan](1%20-%20projeto/PM1.3-release_plan.md)
- [Arquitetura](2%20-%20implementacao/SI3%20-%20inception/diagramas/SI.3-design.md)
