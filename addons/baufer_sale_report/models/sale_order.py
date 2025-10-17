from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vehicle_brand = fields.Char(string='Marca')
    vehicle_model = fields.Char(string='Modelo')
    vehicle_plate = fields.Char(string='Patente')
    vehicle_vin = fields.Char(string='VIN')
    
    customer_branch = fields.Char(string='Sucursal Cliente')
    customer_contact_name = fields.Char(string='Contacto')
    customer_contact_email = fields.Char(string='Email Contacto')
    customer_contact_phone = fields.Char(string='Teléfono Contacto')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_code = fields.Char(string='Código', related='product_id.default_code', readonly=True)
    origin_location = fields.Char(string='Origen', default='SAIC')
