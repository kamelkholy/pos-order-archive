# -*- coding: utf-8 -*-
{
    'name': 'POS Order Archive',
    'version': '18.0.1.0.0',
    'summary': 'Archive and unarchive Point of Sale orders',
    'description': """
        Adds archive/unarchive functionality to POS Orders.

        Features:
        - Active field on POS orders enabling archive/unarchive via Actions menu
        - Archived orders hidden from default list view
        - "Archived" ribbon on form view for archived orders
        - Search filter to show archived orders
        - Muted styling for archived orders in list view
    """,
    'author': 'Kamel Elkholy',
    'website': 'https://github.com/kamelkholy/pos-order-archive',
    'support': 'kamelabdelkader17@gmail.com',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_order_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
