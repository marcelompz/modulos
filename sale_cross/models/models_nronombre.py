# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrossNronombre(models.Model):
    _name = 'cross.nronombre'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'


# @api.model
# def create(self, vals):
#    if vals.get('name', _('New')) == _('New'):
#        vals['name'] = self.env['ir.sequence'].next_by_code('cross.nronombre' or _('New')
#    result = super(CrossNronombre, self).create(vals)
#    return result
#name = fields.Char(string='Nronombre id', required=True, copy=False, readonly=True,
                   index=True, default=lambda self: _('New'))
#numero = fields.Char()
#nombre = fields.Char()


# class sale_cross_nronombre(models.Model):
#    _inherit = 'sale.order.line'
#    _description = "Nombre y Nro de Remera1"
#    nronombre_id = fields.Many2one('cross.nronombre', string='Nronombre id')
#    nro_nombre = fields.One2many('sale.order.line', 'nronombre_id', string='Nro y Nombre')
#    number = fields.Char()
#    name = fields.Char()


class sale_cross_nronombre1(models.Model):
    _inherit = 'sale.order'
    _description = "Nombre y Nro de Remera1"
    nronombre_id = fields.Many2one('cross.nronombre', string='Nronombre id')
    nro_nombre = fields.One2many('sale.order', 'nronombre_id', string='Nro y Nombre')
    number = fields.Char()
    name = fields.Char()

# @api.model
# def create(self, vals):

# _name = 'sale.cross.nronombre'
#      cod = fields.Char('cod')
#      name = fields.Char('name')
#      nro = fields.Char('nro')

#             value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#
