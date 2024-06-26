from pydantic import Field
from nomad.config.models.plugins import SchemaPackageEntryPoint


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Config parameter for this plugin.')

    def load(self):
        from nomad_example.schema_packages.mypackage import m_package
        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)

