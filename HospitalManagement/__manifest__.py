{
    'name': 'Hospital Management',
    'version': '1.1',
    'sequence': 1,
    'author': 'Planet Odoo',
    'description': """Module Of Sanmeet""",
    'category': '',
    'website': '',
    'depends': [
        'base'
    ],
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/patient_details_view.xml'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
