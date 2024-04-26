from typing import Dict

from nomad.config import config
from nomad.datamodel import EntryArchive
from nomad.parsing.parser import MatchingParser

from nomad_example.schema_packages.mypackage import MySchema

configuration = config.get_plugin_entry_point('nomad_example.parsers:myparser')


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: Dict[str, EntryArchive] = None,
    ) -> None:
        logger.info(f'MyParser.parse: parameter={configuration.parameter}')
        archive.data = MySchema()
        archive.data.name = 'Value from parser'