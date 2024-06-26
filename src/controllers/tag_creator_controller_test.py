import os
from unittest.mock import patch

from src.drivers.barcode_handler import BarcodeHandler

from .tag_creator_controller import TagCreatorController


@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = "image_name"
    mock_create_barcode.return_value = f"{mock_value}.png"
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1

    expected_path = os.path.abspath(
        os.path.join("barcodes", f"{mock_value}.png"))
    assert result["data"]["path"] == expected_path
