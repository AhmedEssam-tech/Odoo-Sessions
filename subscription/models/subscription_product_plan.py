from odoo import api, fields, models


class ProductTemplates(models.Model):
    _name = "product"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = "Product"


    name = fields.Char('Name', required=True, translate=True)
    description = fields.Html('Description', translate=True)
    sale_ok= fields.Boolean('Sales', default=True)
    purchase_ok= fields.Boolean('Purchases', default=True)
    subscriptions_ok= fields.Boolean('Subscriptions', default=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")
    pricelist_ids=fields.One2many('product_recurring','prices_id')


#     general information____________________________________________________
    product_type=fields.Selection([('goods','Goods'),
                                   ('service','Service'),
                                   ('combo','Combo')])
    create_on_order=fields.Selection([('no','Nothing'),
                                   ('task','Task'),
                                   ('project_task','project and task'),
                                   ('project','project')])
    invoicing_policy=fields.Selection([('','')])
    product_tooltip=fields.Char(readonly=1)
    plan_service=fields.Boolean('Plan Service')
    sales_price=fields.Float('Sales Price',default=1.0)
    sales_Taxes=fields.Many2many('account.tax',string="Sales Taxes")
    cost=fields.Float('Cost')
    purchase_taxes=fields.Many2many('account',string="Purchase Taxes")
    category=fields.Many2one('product.category')
    reference=fields.Char()
    company_id = fields.Many2one('res.company', 'Company')
    internal=fields.Text()





#     accounting___________________________________________________________
    income_account=fields.Many2one('account.account')
    expense_account=fields.Many2one('account.account')
    price_difference_account=fields.Many2one('account.account')

#     sales___________________________________________________________
    optional_products_ids = fields.Char( string='Optional Products')
    optional_tags_ids = fields.Char(string='Tags')
    re_invoice_costs = fields.Selection([('no', 'NO'),
                                         ('cost', 'At cost'),
                                         ('sales_price', 'sales price')])
    description_sales = fields.Text()

#     purchase___________________________________________________________
    info_ids=fields.One2many('product_supplerinfo','suppler_id')
    subcontract_service = fields.Boolean()
    control_policy = fields.Selection([('purchase', 'On ordered quantities'),
                                       ('receive', 'On received quantities')])
    description_purchase = fields.Text()
    subcontract_service = fields.Boolean()
    control_policy = fields.Selection([('purchase', 'On ordered quantities'),
                                       ('receive', 'On received quantities')])
    description_purchase = fields.Text()


class ProductSuppler(models.Model):
    _name = "product_supplerinfo"


    suppler_id=fields.Many2one('product')
    vendor=fields.Many2one('res.partner',required=1)
    product_name= fields.Char(string="Vendor Product Name")
    product_code = fields.Char(string="Vendor Product Code")
    start_date=fields.Date('Start Date')
    end_date= fields.Date('End Date')
    company_id = fields.Many2one('res.company', 'Company')
    quantity=fields.Float(required=1)
    price=fields.Float(required=1)
    discount=fields.Float('Discount(%)')
    currency=fields.Many2one('res.currency',required=1)
    delivery=fields.Integer(required=1)


#     Recurring Prices_____________________________________________________
class RecuringPrices(models.Model):
    _name = "product_recurring"

    prices_id=fields.Many2one('product')
    recurring_plan=fields.Many2one('subscription.plan',string='Recurring Plan')
    pricelist_id=fields.Many2one('price',string="PriceList")
    price=fields.Float(string='Recurring Price',required=1)


