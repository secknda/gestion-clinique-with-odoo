# -*- coding: utf-8 -*-
# Ce fichier décrit notre module 


{
    'name': 'Gestion Clinique',
    'sequence' : '2',
    ' author' : 'Babacar Seck',
    'version': '0.1',
    'category': 'TP',
    'description': """ Ce module a été crée lors du primer TP odoo 
             pour gérer une clinique ! """,
    'depends': ['base'],
    'data': [
        'views/view_docteur.xml',
        'views/view_domaine.xml',
        'views/view_grade.xml',
        'views/view_patient.xml',
        'views/view_diplome.xml',
        'views/sequence.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
