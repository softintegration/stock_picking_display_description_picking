# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    set_description_pickingout = fields.Boolean('Replace the name of product by the delivery order description in the Delivery report', default=False)
