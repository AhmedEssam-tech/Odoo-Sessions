from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SubscriptionPlan(models.Model):
    _name = 'subscription.plan'
    _description = 'subscription.plan'

    name = fields.Date(string='Name')
    billing_cycle = fields.Selection([('monthly' , 'Monthly') , ('annual' , 'Annual')] , default ='monthly')
    base_price = fields.Float(string='Base Price')
    renew  = fields.Boolean(default=True , string="Renew")
    # subscription_pricing_id = fields.One2many('subscription.pricing',  'subscription_plan_id', string='Pricing')

    # automatic_closing = fields.Integer(string='Auutomatic Closing')




