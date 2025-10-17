{
    'name': 'BAUFER - CRM Personalizado',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Pipeline CRM personalizado según proceso BAUFER',
    'description': '''
        Módulo que personaliza el CRM de Odoo según el blueprint BAUFER.
        
        Características:
        - Estados personalizados del pipeline
        - Score BANT (Budget, Authority, Need, Timeline)
        - Automatizaciones de primer contacto
        - Asignación automática por territorio
        - Checklist de discovery
        - Campos de importación (Incoterm, necesidad)
        - Integración con módulo de ventas
    ''',
    'author': 'BAUFER - Inversiones Séneca SpA.',
    'website': 'https://www.baufer.cl',
    'depends': ['crm', 'sale_crm', 'baufer_sale_report'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_stage_data.xml',
        'data/automated_actions.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

