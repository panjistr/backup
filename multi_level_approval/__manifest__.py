# -*- coding: utf-8 -*-
{
    'name': 'Odoo Approval',
    'version': '14.0.1.1',
    'category': 'Approvals',
    'description': """
    """,
    'summary': '''
    Create and validate approval requests. Each request can be approved by many levels of different managers
    ''',
    'depends': [
        'mail',
        'product'
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

        # wizard
        'wizard/refused_reason_views.xml',

        'views/multi_approval_type_views.xml',
        'views/multi_approval_views.xml',

        # Add actions after all views.
        'views/actions.xml',

        # Add menu after actions.
        'views/menu.xml',
        
    ],
    'images': ['static/description/banner.jpg'],
    'test': [],
    'demo': [],
    'installable': True,
    'active': False,
    'application': True,
}
