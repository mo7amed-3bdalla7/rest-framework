import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo==3.1.7'],
    odoo_addon={
        'external_dependencies_override': {
            'python': {
                'accept_language': 'parse-accept-language==0.1.2',
                'apispec': 'apispec==6.0.2'
            },
        },
    }
)
