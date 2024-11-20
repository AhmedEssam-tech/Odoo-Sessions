from email.policy import default

from odoo import models, fields, api
from odoo.api import onchange
from odoo.exceptions import ValidationError


class SubscriptionPlan(models.Model):
    _name = 'subscription.plan'
    _description = 'subscription.plan'

    name = fields.Char(string='Name')
    billing_cycle = fields.Selection([('monthly' , 'Monthly') , ('annual' , 'Annual')] , default ='monthly')
    base_price = fields.Float(string='Base Price')
    renew  = fields.Boolean(default=True , string="Renew")
    subscription_pricing_id = fields.One2many('subscription.pricing',  'subscription_plan_id', string='Pricing')

    # automatic_closing = fields.Integer(string='Auutomatic Closing')



class SubscriptionPricing(models.Model):
    _name = 'subscription.pricing'
    _description = 'subscription.pricing'

    product_id = fields.Many2one('product.template', string="Product")
    recurring_price = fields.Float(string="Recurring Price")
    subscription_plan_id = fields.Many2one('subscription.plan', string='Plan')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.recurring_price = self.product_id.list_price





