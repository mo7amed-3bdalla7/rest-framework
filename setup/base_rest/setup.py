import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo==3.1.12'],
    odoo_addon={
        'external_dependencies_override': {
            'python': {
                'accept_language': 'parse-accept-language',
                'apispec': 'apispec==6.3.0'
            },
        },
    }
)
