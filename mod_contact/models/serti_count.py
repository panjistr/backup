
from odoo import models, fields, api

class SertiCount(models.Model):
    _inherit = 'res.partner'

    revalue_count = fields.Integer(compute='_revalue_count', string='# Revalue Asset')

    def _revalue_count(self):
        for record in self:
            revalue_count = self.env['multi.approval'].search_count([('contact_id', '=', record.id)])
            record.revalue_count= revalue_count
            

    def open_revalues(self):
        return {
            'name': ('Sertifikasi Count'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'multi.approval',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('contact_id', '=', self.id)],
            'target':'new',
            'context': "{'default_asset_id': active_id, 'create': False}"
        }