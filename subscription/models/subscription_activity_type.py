from odoo import models,fields,api
from odoo.exceptions import ValidationError



class Activity_Type(models.Model):
    _name = 'activity.type'
    _description = 'activity type model '
    # _inherit=['mail.thread','mail.activity.mixin']


# default="This is a default text." in xml name view
    name = fields.Char(string='Name',required=True)
    category = fields.Selection([
        ('default', 'None'),
        ('upload_file', 'Upload_File'),
        ('phonecall', 'PhoneCall'),], string='Action',required=True)
    dashboard_visibility = fields.Selection([
        ('none', 'None'),
        ('own', 'Own Activities'),
        ('all', 'all Activities'),], string='Dashboard Visibility',required=True)
    default_user_id=fields.Many2one('res.users', string='Default User', required=True)
    res_model = fields.Selection([
        ('res.partner', 'Contact'),
        ('sales.order', 'Sales Order'),
        ('crm.team', 'Crm Team'),], string='Model')
    # default="This is a default text." in xml name view
    summary = fields.Char(string='Default Summary')
    icon = fields.Char(string='Icon')
    decorating_type = fields.Selection([
        ('warning', 'Alert'),
        ('danger', 'Error'),], string='Decorating Type')
    keep_done=fields.Boolean(string='Keep Done')
    default_note=fields.Char(string='Default Note')
    changing_type = fields.Selection([
        ('suggest', 'Suggest Next Activates'),
        ('trigger', 'Trigger Next Activates'),], string='Changing Type')
    suggest_next_type_ids = fields.Many2many('mail.activity.type', string='Suggest')
    email_template_ids = fields.Many2many('mail.template', string='Email Templates')
    delay_count=fields.Integer(string="Schedule")
    active=fields.Boolean(default=True)
    # date = fields.Date(string='Availability',required=True,tracking=1)