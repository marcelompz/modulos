# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_cross(models.Model):
    _inherit = 'sale.order.line'
    color = fields.Many2one('color.cross')
    project = fields.Many2one("project.project")

    nronombre_id = fields.Many2many(
    comodel_name='nro.nombre',
    relation='nronombre_id_rel',
    column1='name',
    column2='number',
    string='Nro y nombre de la remera',
)


class sale_cross_adjunto(models.Model):
    _inherit = 'sale.order'
    attachment_id = fields.Many2many(
        comodel_name='ir.attachment',
        relation='attachments_rel',
        column1='account_id',
        column2='attachment_id',
        string='Archivo Adjunto',
    )
#    nronombre_id = fields.Many2many(
#        comodel_name='nro.nombre',
#        relation='nronombre_id_rel',
#        column1='name',
#        column2='number',
#        string='Nro y nombre de la remera',
#    )


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    def onchange_template_id(self,
                             template_id,
                             composition_mode,
                             model,
                             res_id):
        r = super(MailComposer, self).onchange_template_id(template_id,
                                                           composition_mode,
                                                           model,
                                                           res_id)
        ai_id = self._context['active_ids'][0]
        ids = []
        for line in self.env['sale.order'].search([('id', '=', ai_id)]):
            for lines_attachment in line.attachment_ids:
                ids.append(lines_attachment.id)
        if r['value']['attachment_ids']:
            ids.insert(0, r['value']['attachment_ids'][0])
            r['value']['attachment_ids'] = ids
        return

    def onchange_template_id(self,
                             template_id,
                             composition_mode,
                             model,
                             res_id):
        r = super(MailComposer, self).onchange_template_id(template_id,
                                                           composition_mode,
                                                           model,
                                                           res_id)
        ai_id = self._context['active_ids'][0]
        ids = []
        for line in self.env['sale.order.line'].search([('id', '=', ai_id)]):
            for lines_nronombre in line.nronombre_ids:
                ids.append(lines_nronombre.id)
        if r['value']['nronombre_ids']:
            ids.insert(0, r['value']['nronombre_ids'][0])
            r['value']['nronombre_ids'] = ids
        return
