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
        'wizards/patient_wizard.xml',
        'views/patient_details_view.xml',
        'views/doctors_details_view.xml',
        'views/inherit_in_doctors_view.xml',
        'views/gender_view.xml',

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
