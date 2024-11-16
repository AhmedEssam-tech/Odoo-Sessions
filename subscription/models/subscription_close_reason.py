from odoo import models,fields,api

class SaleOrderCloseReason(models.Model):
    _name = "sale.order.close.reason"
    _description = "Subscription Close Reason"

    name = fields.Char('Reason', required=True, translate=True)

    visible_in_portal = fields.Boolean(default=True, required=True)