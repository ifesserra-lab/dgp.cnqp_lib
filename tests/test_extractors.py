from unittest.mock import MagicMock

from dgp_cnpq_lib.extractors import BaseExtractor, FieldsetParser, TableExtractor


class TestBaseExtractor:
    def test_normalize_key(self):
        assert BaseExtractor.normalize_key("Área de Atuação") == "area_de_atuacao"
        assert BaseExtractor.normalize_key("Nome:") == "nome"
        assert BaseExtractor.normalize_key("  Espaços  ") == "espacos"

    def test_clean_value(self):
        assert BaseExtractor.clean_value("  Valor   Teste  ") == "Valor Teste"
        assert BaseExtractor.clean_value("") == ""


class TestTableExtractor:
    def test_extract_empty_table(self):
        extractor = TableExtractor()
        mock_table = MagicMock()
        mock_table.query_selector_all.return_value = []  # headers empty

        assert extractor.extract(mock_table) == []


class TestFieldsetParser:
    def test_init(self):
        parser = FieldsetParser()
        assert isinstance(parser.table_extractor, TableExtractor)
