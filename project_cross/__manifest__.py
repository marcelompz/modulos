# -*- coding: utf-8 -*-
{
    'name': "project_cross",

    'summary': """
        Project custom module, with new features""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Crossnexion EAS",
    'website': "http://www.crossnexion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project','sale','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
