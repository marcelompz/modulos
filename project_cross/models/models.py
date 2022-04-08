# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project_cross(models.Model):
    _inherit = "project.project"
    benefit = fields.Char()
    objetive = fields.Char()


class project_task_cross(models.Model):
    _inherit = "sale.order"
    attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='attachments_rel',
        column1='account_id',
        column2='attachment_id',
        string='Archivo Adjunto',
    )

#    @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
