from _datetime import datetime
import io
import json

import allure
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from conftest import LOGGER


def read_file(file_path):
    LOGGER.info("Read data from file: '{}'".format(file_path))
    with open(file_path) as f:
        data = json.loads(f.read())
    return data

@allure.step("Check values in pdf file")
def check_pdf(file_pdf, checking_values, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(file_pdf, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    text_rep_1 = text.replace(" \n\n\x0c", "")
    text_replace_2 = text_rep_1.replace(" \n\n", "\n")
    print(text_replace_2)
    output.close()
    try:
        assert text_replace_2 == checking_values
    except AssertionError:
        LOGGER.error(f"Text in pdf file doesn't contain expected text")
        raise AssertionError(f"Text in pdf file doesn't contain expected text")