from typing import TYPE_CHECKING

from nomad.config import config
from nomad.parsing.parser import MatchingParser

from nomad_plugin_fitness.schema_packages.schema_package import DailyFitnessSummary

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


configuration = config.get_plugin_entry_point(
    'nomad_plugin_fitness.parsers:parser_entry_point'
)


class FitnessParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('FitnessParser.parse', parameter=configuration.parameter)

        archive.data = DailyFitnessSummary(source_file=mainfile)
