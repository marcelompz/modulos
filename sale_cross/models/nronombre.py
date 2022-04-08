# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nronombre_cross(models.Model):
    _name = 'nro.nombre'
    cod = fields.Char('Cod', required=True)
    name = fields.Char('Nombre', required=False)
    number = fields.Char('Numero', required=False)
#             value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#
