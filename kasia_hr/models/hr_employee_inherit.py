from odoo import fields, models, api

class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee' 

    bank_code = fields.Char(string='Bank Code', size=5)
    agency_code = fields.Char(string='Agency Code', size=5)
    account_number = fields.Char(string='Account Number', size=11)
    rib_key = fields.Char(string='RIB Key', size=2)
    bank_id = fields.Char(string='Bank ID') 

    # Champ calculé pour le RIB complet
    full_rib = fields.Char(string='RIB Complet', compute='_compute_full_rib', store=True)

    # Méthode de calcul pour le champ full_rib
    @api.depends('bank_code', 'agency_code', 'account_number', 'rib_key')
    def _compute_full_rib(self):
        for employee in self:
            bank_code = employee.bank_code or ''
            agency_code = employee.agency_code or ''
            account_number = employee.account_number or ''
            rib_key = employee.rib_key or ''
            employee.full_rib = f"{bank_code} {agency_code} {account_number} {rib_key}".strip()