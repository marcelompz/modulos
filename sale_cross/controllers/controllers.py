# -*- coding: utf-8 -*-
from odoo import http


# class SaleCross(http.Controller):
#     @http.route('/sale_cross/sale_cross/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_cross/sale_cross/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_cross.listing', {
#             'root': '/sale_cross/sale_cross',
#             'objects': http.request.env['sale_cross.sale_cross'].search([]),
#         })

#     @http.route('/sale_cross/sale_cross/objects/<model("sale_cross.sale_cross"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_cross.object', {
#             'object': obj
#         })
