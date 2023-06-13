import os.path
import tempfile
from griptape.artifacts import BlobArtifact, ListArtifact
from griptape.tools import FileManager


class TestFileManager:
    def test_load_from_disk(self):
        result = FileManager(
            dir=os.path.abspath(os.path.dirname(__file__))
        ).load_from_disk({"values": {"paths": ["resources/bitcoin.pdf"]}})

        assert isinstance(result, ListArtifact)
        assert len(result.value) == 1
        assert isinstance(result.value[0], BlobArtifact)

    def test_save_to_disk(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = os.path.join(temp_dir, "foobar.txt")
            artifact = BlobArtifact(b"foobar", name="test.txt")
            result = FileManager().save_to_disk({"values": {"paths": [path]}, "artifacts": {"values": [artifact]}})

            assert result.value == "saved successfully"
