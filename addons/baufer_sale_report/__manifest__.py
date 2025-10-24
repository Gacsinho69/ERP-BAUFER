{
    'name': 'BAUFER - Reportes de Venta Personalizados',
    'version': '19.0.2.0.0',
    'category': 'Sales',
    'summary': 'Cotizaciones profesionales con diseño minimalista y elegante',
    'description': '''
        Módulo que personaliza los reportes de cotización y pedidos de venta
        con un diseño corporativo profesional y minimalista de BAUFER.

        Características principales:
        ✓ Diseño minimalista y ultra profesional
        ✓ Paleta de colores GULF (Azul #003D7A, Naranja #FF6200)
        ✓ Tipografía moderna y jerarquía visual clara
        ✓ Tabla de productos limpia con líneas sutiles
        ✓ Sección de totales elegante y destacada
        ✓ Campos personalizados de vehículo (Marca, Modelo, Patente, VIN)
        ✓ Información de contacto mejorada y organizada
        ✓ Columnas de código de producto y origen
        ✓ Optimizado para impresión PDF de alta calidad
        ✓ Responsive y adaptable a diferentes tamaños

        Versión 2.0.0: Rediseño completo con enfoque minimalista
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

