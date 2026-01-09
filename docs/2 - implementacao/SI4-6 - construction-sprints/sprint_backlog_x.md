# Sprint Backlog Template
**Sprint:** <Número>
**Período:** <Data Início> a <Data Fim>
**Meta:** <Objetivo Principal da Sprint>
**Responsável:** <Nome do Facilitador/Scrum Master>

---

# 1. Itens Selecionados (Sprint Backlog)

## US-XXX – <Título da User Story>
**Origem:** <Backlog / Issue #ID>
**Responsável:** @user
**Estimativa:** <Pontos/Horas>

### Tasks
- [ ] **DEV**: <Descrição da Implementação>
- [ ] **TEST**: <Descrição dos Testes Unitários/Integração>
- [ ] **DOCS**: <Atualização de Documentação Técnica>

---

# 2. Daily Log
| Data | Progresso | Impedimentos |
|------|-----------|--------------|
| DD/MM | ... | ... |

---

# 3. Definition of Done (DoD) - Sprint Check
Para considerar a Sprint concluída, todos os itens devem atender:

### Verificação
- [ ] **Testes**: Suíte de testes passando (Unitários + Integração).
- [ ] **Linting**: Código em conformidade com `black`, `flake8`, `isort`.
- [ ] **OO Compliance**: Uso estrito de Classes e Encapsulamento.

### Documentação
- [ ] **Docstrings**: Google-style docstrings em todas as classes/métodos.
- [ ] **Docs**: Atualização de `docs/*.md` pertinentes.
- [ ] **Walkthrough**: Evidências de funcionamento (se aplicável).

### Encerramento
- [ ] Pull Request mergeado em `developing` (ou `master` se Release).
- [ ] Branches locais e remotas deletadas.
- [ ] Backlog atualizado.
