# Project Plan
**Projeto:** dgp.cnqp_lib
**Data:** 09/01/2026
**Autor:** Antigravity (Senior PM)
**Versão:** 2.0

---

# 1. Escopo e WBS (PM1.2)
A estrutura analítica do projeto (EAP/WBS):

1.  **Fundação (Sprint 0)**
    1.1. Setup de estrutura do projeto (OO).
    1.2. Definição de Classes (`CnpqCrawler`, `Extractors`).
2.  **Extração Básica (Sprint 1)**
    2.1. Implementar `BaseExtractor` e `TableExtractor`.
    2.2. Implementar `FieldsetParser`.
    2.3. Implementar `CnpqCrawler`.
3.  **CLI e Saída JSON (Sprint 2)**
    3.1. Criar `__main__.py` para interface CLI.
    3.2. Garantir saída JSON dinâmica (nomeada após o grupo).
4.  **Testes e Documentação (Sprint 3)**
    4.1. Implementar testes unitários (`pytest`).
    4.2. Atualizar documentação técnica (`SI1`, `SI2`).
    4.3. Criar `README.md` técnico.

---

# 2. Cronograma Macro (PM1.3)
| Marco | Descrição | Status |
|-------|-----------|--------|
| **S0** | Fundação OO | ✅ Completo |
| **S1** | Extração Básica | ✅ Completo |
| **S2** | CLI e JSON | ✅ Completo |
| **S3** | Testes e Docs | ✅ Completo |

---

# 3. Recursos (PM1.4)
- **Equipe Técnica**: 1 Desenvolvedor Python (User).
- **Tecnologia**: Python 3.8+, Playwright, Pytest.

---

# 4. Plano de Gerenciamento de Riscos (PM1.7)
| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Mudanças no Layout do CNPq | Alto | Testes manuais periódicos; manter classes encapsuladas para facilitar updates. |
| Falhas no Playwright | Médio | Retry logic e tratamento de exceções. |

---

# 5. Critérios de Aceite (PM1.8)
- A biblioteca deve extrair dados via `python -m dgp_cnpq_lib <url>`.
- Saída JSON nomeada dinamicamente após o grupo.
- Todos os testes passando (`pytest`).
- Código limpo (`black`, `flake8`, `isort`).
