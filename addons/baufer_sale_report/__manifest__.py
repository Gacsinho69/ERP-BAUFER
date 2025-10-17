{
    'name': 'BAUFER - Reportes de Venta Personalizados',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Cotizaciones personalizadas estilo BAUFER/SAP',
    'description': '''
        Módulo que personaliza los reportes de cotización y pedidos de venta
        con el diseño corporativo de BAUFER.
        
        Características:
        - Diseño profesional con colores GULF (azul #003D7A y naranja #FF6200)
        - Campos de vehículo (Marca, Modelo, Patente, VIN)
        - Información de contacto mejorada
        - Columna de código y origen en productos
        - Reporte PDF personalizado estilo SAP
    ''',
    'author': 'BAUFER - Inversiones Séneca SpA.',
    'website': 'https://www.baufer.cl',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
        'reports/sale_report_templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'baufer_sale_report/static/src/css/report_style.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

