from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Subscription(models.Model):
    _name = 'the.subscription'
    _description = 'the.subscription'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    total_price = fields.Float(string='Total Price')
    # customer_id = fields.Many2one('res.partner', string="Customer")
    # plan_id = fields.Many2one('subscription.plan', string="Subscription Plan", required=True)


