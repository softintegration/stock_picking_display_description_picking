# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    set_description_pickingout = fields.Boolean(related='product_tmpl_id.set_description_pickingout',store=True)
