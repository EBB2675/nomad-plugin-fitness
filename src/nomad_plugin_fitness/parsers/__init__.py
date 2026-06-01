from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class FitnessParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_plugin_fitness.parsers.parser import FitnessParser

        return FitnessParser(**self.model_dump())


parser_entry_point = FitnessParserEntryPoint(
    name='FitnessParser',
    description='Parser entry point for smart wearable and fitness data.',
    mainfile_name_re=r'.*\.(xml|XML|health\.xml|apple_health\.xml)$',
)
