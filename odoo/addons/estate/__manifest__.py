# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Buy and sell houses',
    'depends': [
        'base_setup',
    ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
# Order matters. Esure all views are loaded before the menus.
        'views/estate_menus.xml',
    ],
    'author': 'Justin Skootsky',
    'license': 'LGPL-3',
}