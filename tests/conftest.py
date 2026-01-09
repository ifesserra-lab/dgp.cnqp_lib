from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_page_content():
    return """
    <html>
        <body>
            <h1>Grupo de Teste</h1>
            <fieldset>
                <legend>Dados Gerais</legend>
                <label class="control-label">Nome do Grupo:</label>
                <div><span>Grupo de Teste</span></div>
                
                <label class="control-label">Líderes do grupo:</label>
                <div><span>João da Silva<br>Maria Santos</span></div>
            </fieldset>
            
            <fieldset>
                <legend>Linhas de pesquisa</legend>
                <table>
                    <thead>
                        <tr><th>Título</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>IA Aplicada</td></tr>
                        <tr><td>Visão Computacional</td></tr>
                    </tbody>
                </table>
            </fieldset>
        </body>
    </html>
    """


@pytest.fixture
def mock_element_handle():
    """Mock for Playwright ElementHandle"""
    mock = MagicMock()
    return mock
