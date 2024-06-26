from nomad.datamodel import EntryArchive
from nomad_example.parsers.myparser import MyParser
import logging


def test_parse_file():
    parser = MyParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())

    assert archive.data.name == 'Value from parser'