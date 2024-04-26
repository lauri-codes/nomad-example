from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus, Filters

schema1 = 'nomad_example.schema_packages.mypackage.MySchema'


myapp = AppEntryPoint(
    name='MyApp',
    description='App defined using the new plugin mechanism.',
    app = App(
        label='MyApp',
        path='myapp',
        category='simulation',
        columns=Columns(
            selected=['entry_id', f'data.name#{schema1}'],
            options={
                'entry_id': Column(),
                f'data.name#{schema1}': Column(label='Name')
            }
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label="Material"),
                'eln': FilterMenu(label="ELN")
            }
        ),
        filters=Filters(include=['*#nomad_example.schema_packages.*']),
        filters_locked={
            'section_defs.definition_qualified_name': schema1
        }
    )
)