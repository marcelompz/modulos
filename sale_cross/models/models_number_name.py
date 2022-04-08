# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrossNronombre(models.Model):
    _name = 'nro.name'
    cod = fields.Char('Cod', required=True)
    name = fields.Char('Nombre', required=False)
    number = fields.Char('Numero', required=False)


class CrossNronombre2(models.Model):
    _name = 'nro.name.a'
    numbername_id = fields.Many2one('nro.name', string='numbername_id')


class CrossNronombre3(models.Model):
    _inherit = 'sale.order'
    nro_nombre = fields.One2many('nro.name.a', 'numbername_id', string='nro_nombre')
