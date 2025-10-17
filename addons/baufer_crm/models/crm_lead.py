from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Score BANT
    bant_budget = fields.Selection([
        ('0', 'No definido'),
        ('25', 'Bajo presupuesto'),
        ('50', 'Presupuesto medio'),
        ('75', 'Buen presupuesto'),
        ('100', 'Presupuesto confirmado'),
    ], string='Budget (Presupuesto)', default='0', help='¿Tiene presupuesto definido?')
    
    bant_authority = fields.Selection([
        ('0', 'No es decisor'),
        ('25', 'Influenciador'),
        ('50', 'Parte del comité'),
        ('75', 'Co-decisor'),
        ('100', 'Decisor único'),
    ], string='Authority (Autoridad)', default='0', help='¿Es el decisor de compra?')
    
    bant_need = fields.Selection([
        ('0', 'Sin necesidad clara'),
        ('25', 'Necesidad exploratoria'),
        ('50', 'Necesidad identificada'),
        ('75', 'Necesidad urgente'),
        ('100', 'Necesidad crítica'),
    ], string='Need (Necesidad)', default='0', help='¿Qué tan urgente es la necesidad?')
    
    bant_timeline = fields.Selection([
        ('0', 'Sin timeline'),
        ('25', '>6 meses'),
        ('50', '3-6 meses'),
        ('75', '1-3 meses'),
        ('100', '<1 mes'),
    ], string='Timeline (Plazo)', default='0', help='¿Cuándo planea comprar?')
    
    bant_score = fields.Integer(string='Score BANT', compute='_compute_bant_score', store=True)
    
    # Campos de importación
    incoterm_expected = fields.Selection([
        ('exw', 'EXW - Ex Works'),
        ('fca', 'FCA - Free Carrier'),
        ('cpt', 'CPT - Carriage Paid To'),
        ('cip', 'CIP - Carriage and Insurance Paid To'),
        ('dpu', 'DPU - Delivered at Place Unloaded'),
        ('dap', 'DAP - Delivered at Place'),
        ('ddp', 'DDP - Delivered Duty Paid'),
        ('fas', 'FAS - Free Alongside Ship'),
        ('fob', 'FOB - Free on Board'),
        ('cfr', 'CFR - Cost and Freight'),
        ('cif', 'CIF - Cost, Insurance and Freight'),
    ], string='Incoterm Previsto', help='Incoterm esperado para la operación')
    
    need_documented = fields.Text(string='Necesidad Documentada', 
                                   help='Descripción detallada de la necesidad del cliente')
    
    discovery_checklist = fields.Selection([
        ('pending', 'Pendiente'),
        ('partial', 'Parcial'),
        ('complete', 'Completo'),
    ], string='Discovery', default='pending', help='Estado del checklist de discovery')
    
    territory = fields.Selection([
        ('santiago', 'Santiago'),
        ('norte', 'Zona Norte'),
        ('sur', 'Zona Sur'),
        ('centro', 'Zona Centro'),
        ('internacional', 'Internacional'),
    ], string='Territorio', help='Territorio comercial')
    
    lead_origin = fields.Selection([
        ('web', 'Sitio Web'),
        ('email', 'Email'),
        ('phone', 'Teléfono'),
        ('referral', 'Referido'),
        ('event', 'Evento/Feria'),
        ('linkedin', 'LinkedIn'),
        ('other', 'Otro'),
    ], string='Origen del Lead', help='¿Cómo llegó este lead?')
    
    first_contact_date = fields.Datetime(string='Primer Contacto', readonly=True,
                                          help='Fecha del primer contacto efectivo')
    
    @api.depends('bant_budget', 'bant_authority', 'bant_need', 'bant_timeline')
    def _compute_bant_score(self):
        """Calcula el score BANT total (promedio de los 4 criterios)"""
        for lead in self:
            scores = [
                int(lead.bant_budget),
                int(lead.bant_authority),
                int(lead.bant_need),
                int(lead.bant_timeline),
            ]
            lead.bant_score = sum(scores) // 4 if any(scores) else 0
    
    @api.model
    def create(self, vals):
        """Al crear un lead, programar actividad de primer contacto"""
        lead = super().create(vals)
        
        # Crear actividad automática de primer contacto (SLA 15 minutos)
        if not lead.activity_ids:
            lead.activity_schedule(
                'mail.mail_activity_data_call',
                summary='⚡ Primer contacto (SLA 15 min)',
                note='Contactar al lead por primera vez. SLA: 15 minutos desde creación.',
                date_deadline=fields.Date.today(),
                user_id=lead.user_id.id or self.env.user.id
            )
        
        return lead
    
    def action_set_won(self):
        """Al ganar una oportunidad, crear sale order y carpeta de documentos"""
        res = super().action_set_won()
        
        for lead in self:
            # Crear sale order si no existe
            if not lead.order_ids:
                sale_order = self.env['sale.order'].create({
                    'partner_id': lead.partner_id.id,
                    'opportunity_id': lead.id,
                    'user_id': lead.user_id.id,
                    'team_id': lead.team_id.id,
                    'campaign_id': lead.campaign_id.id,
                    'medium_id': lead.medium_id.id,
                    'source_id': lead.source_id.id,
                })
                
                # Copiar datos del lead al sale order
                if lead.incoterm_expected:
                    sale_order.incoterm = self.env['account.incoterms'].search(
                        [('code', '=', lead.incoterm_expected.upper())], limit=1
                    )
            
            # TODO: Crear carpeta en Documents cuando se implemente ese módulo
            # documents_folder = self.env['documents.folder'].create({
            #     'name': f'Operación {lead.name}',
            #     'parent_folder_id': ref_to_operations_folder,
            # })
        
        return res
    
    def action_mark_first_contact(self):
        """Marcar que se hizo el primer contacto"""
        for lead in self:
            if not lead.first_contact_date:
                lead.first_contact_date = fields.Datetime.now()

