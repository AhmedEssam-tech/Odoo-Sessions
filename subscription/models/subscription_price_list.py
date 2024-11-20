from odoo import api, fields, models

class ProductPrices(models.Model):
    _name = "price"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']

    name=fields.Char(string="Name",required=1)
    currency=fields.Many2one('res.currency', string="Currency")
    company= fields.Many2one('res.company',string="Company")
    country_groups=fields.Many2many('res.country.group',string="Country Groups")
    price_ids=fields.One2many('product_recurring','prices_id')
    rules_ids = fields.One2many('price_rules', 'rules_id')



class SubRecuringPrices(models.Model):
    _name = "subscription_price"

    prices_id=fields.Many2one('product',string='Product')
    recurring_plan=fields.Many2one('subscription.plan',string='Recurring Plan')
    price=fields.Float(string='Recurring Price',required=1)


class PriceRules(models.Model):
    _name = "price_rules"

    rules_id = fields.Many2one('price')
    name=fields.Char(readonly=1)
    price = fields.Char(readonly=1)
    min_quantity = fields.Float()
    start_date = fields.Datetime()
    end_date = fields.Datetime()

