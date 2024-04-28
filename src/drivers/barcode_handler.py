import os

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())

        barcodes_folder = "barcodes"
        if not os.path.exists(barcodes_folder):
            os.makedirs(barcodes_folder)
        filename = os.path.join(barcodes_folder, f'{product_code}')

        tag.save(filename)

        return filename
