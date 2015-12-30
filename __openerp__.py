# -*- coding: utf-8 -*-
{
    'name': 'Home Management',
    'version': '1.0',
    'category': 'Home',
    'sequence': 1,
    'summary': 'Home, smart objects, PIs',
    'description': """
    """,
    'author': 'Valentin Thirion',
    'website': 'http://www.medineo.be',
    'depends': ['report'],
    'data': [
        'views/home.xml',
        'views/appliance.xml',
        'views/appliances_group.xml',
        'views/mode.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: