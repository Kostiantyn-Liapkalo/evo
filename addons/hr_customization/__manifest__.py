# -*- coding: utf-8 -*-
{
    'name': "HR Customization",
    'summary': "Customizations for HR management including positions and organization charts.",
    'description': """
This module provides various customizations for HR management in Odoo. 
It includes features such as managing employee positions, custom fields in the employee form, 
and enhancements to the organization chart.
    """,
    'author': "Kostiantyn Liapkalo",
    'category': 'Human Resources',
    'version': '17.0.0.1.9',
    'depends': ['base', 'hr', 'hr_recruitment', 'hr_skills', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/employee_position_views.xml',
        'views/organization_chart_template.xml',
        'views/hr_job_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'employee_position/static/src/js/organization_chart.js',
        ],
    },
    'application': True,
    'installable': True,
}
