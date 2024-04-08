# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _

PRODUCT_MOD_HISTORY_TRACE_MODULE = 'stock_picking_products_name_history'

class StockMove(models.Model):
    _inherit = "stock.move"


    def _product_mod_history_trace_module(self):
        installed = self.env['ir.module.module'].search_count([('name','=',PRODUCT_MOD_HISTORY_TRACE_MODULE),('state','=','installed')]) > 0
        return installed
