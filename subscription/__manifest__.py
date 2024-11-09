{
    'name': "Subscriptions",

    'summary': "Subscriptions With Complicated Pricing System",

    'description': "Subscriptions With Complicated Pricing System",

    'author': "odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
    ],
    'assets' :{
    },
    # only loaded in demonstration mode
    'demo': [
    ],
}