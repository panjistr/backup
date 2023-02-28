# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crystal_mod_accountasset_button_revalueasset(models.Model):
#     _name = 'crystal_mod_accountasset_button_revalueasset.crystal_mod_accountasset_button_revalueasset'
#     _description = 'crystal_mod_accountasset_button_revalueasset.crystal_mod_accountasset_button_revalueasset'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
