from odoo import models, fields
from odoo.addons.mail.models.mail_thread import MailThread

class ProductAttribution(models.Model,MailThread):
    _name = 'product.attribution' # Nom technique unique du modèle (convention : nom_module.nom_modele_singulier_en_minuscule)
    _description = 'Product Attribution' # Description lisible du modèle

    reference = fields.Char(string="Référence", default="New")
    employee_id = fields.Many2one('hr.employee', string="Employé", required=True)
    product_id = fields.Many2one('product.template', string="Matériel", required=True)
    delivery_date = fields.Date(string="Date de délivrance", required=True, default=fields.Date.today)
    serial_number = fields.Char(string="Numéro de série")
    value = fields.Float(string="Valeur du matériel",related='product_id.list_price')

    category_id = fields.Many2one('product.category', string="Catégorie du matériel")

    note = fields.Html(string="Note")

    assigned_by_id = fields.Many2one(
        'res.users', string="Attribué par",
        default=lambda self: self.env.user,#met utilisateur connecte par defaut 
        readonly=True, 
        help=" Odoo users who created attribution"
    )

    state = fields.Selection([
        ('new', 'Nouveau'),
        ('assigned', 'Attribué'),
        ('returned', 'Retourné'),
        ('lost', 'Perdu'),
        ('broken', 'Cassé'),
        ('refunded', 'Remboursé'),
        ('cancelled', 'Annulé'),
    ], string="État", default='new', tracking=True)

    def action_assign(self):
        """
        Passe l'état de l'attribution à 'Attribué'.
        """
        self.ensure_one() 
        self.write({'state': 'assigned'})
        return True 

    def action_return(self):
        """
        Passe l'état de l'attribution à 'Retourné'.
        """
        self.ensure_one()
        self.write({'state': 'returned'})
        return True

    def action_cancel(self):
        """
        Passe l'état de l'attribution à 'Annulé'.
        """
        self.ensure_one()
        self.write({'state': 'cancelled'})
        return True

    # def action_report_product_attribution_decharge(self):
    #     return self.env.ref('ks_equipment.report_product_attribution_decharge').report_action(self)

