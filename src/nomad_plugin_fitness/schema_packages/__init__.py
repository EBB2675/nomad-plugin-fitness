from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class FitnessSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_plugin_fitness.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = FitnessSchemaPackageEntryPoint(
    name='FitnessSchemaPackage',
    description='Schema package for smart wearable and fitness data.',
)
