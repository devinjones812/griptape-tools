import pytest
from griptape.artifacts import BaseArtifact


class TestWebScraper:
    @pytest.fixture
    def scraper(self):
        from griptape.tools import WebScraper

        return WebScraper()

    def test_get_title(self, scraper):
        assert isinstance(scraper.get_title({
            "values": {"url": "https://github.com/griptape-ai/griptape-tools"}
        }), BaseArtifact)

    def test_get_content(self, scraper):
        assert isinstance(scraper.get_content({
            "values": {"url": "https://github.com/griptape-ai/griptape-tools"}
        }), BaseArtifact)

    def test_get_authors(self, scraper):
        assert isinstance(scraper.get_author({
            "values": {"url": "https://github.com/griptape-ai/griptape-tools"}
        }), BaseArtifact)
