from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Campos para vehículos
    vehicle_brand = fields.Char(
        string='Marca',
        help='Marca del vehículo (ej: Mercedes Benz, Volvo, Scania)'
    )
    vehicle_model = fields.Char(
        string='Modelo',
        help='Modelo del vehículo (ej: O500, 9700, K360)'
    )
    vehicle_plate = fields.Char(
        string='Patente',
        help='Patente del vehículo'
    )
    vehicle_vin = fields.Char(
        string='VIN',
        help='Vehicle Identification Number (Número de chasis)'
    )
    
    # Información adicional del cliente
    customer_branch = fields.Char(
        string='Sucursal Cliente',
        help='Sucursal o sede del cliente'
    )
    customer_contact_name = fields.Char(
        string='Contacto',
        help='Nombre de la persona de contacto'
    )
    customer_contact_email = fields.Char(
        string='Email Contacto',
        help='Email del contacto directo'
    )
    customer_contact_phone = fields.Char(
        string='Teléfono Contacto',
        help='Teléfono del contacto directo'
    )
    
    @api.constrains('customer_contact_email')
    def _check_contact_email(self):
        """Validar formato de email si se ingresa"""
        for record in self:
            if record.customer_contact_email:
                import re
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_pattern, record.customer_contact_email):
                    raise ValidationError('El formato del email de contacto no es válido.')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_code = fields.Char(
        string='Código',
        related='product_id.default_code',
        readonly=True,
        store=True
    )
    origin_location = fields.Selection([
        ('saic', 'SAIC'),
        ('europa', 'Europa'),
        ('asia', 'Asia'),
        ('nacional', 'Nacional'),
        ('eeuu', 'EEUU'),
        ('otro', 'Otro'),
    ], string='Origen', default='saic', help='Origen del repuesto')

