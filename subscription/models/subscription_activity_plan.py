from email.policy import default

from odoo import api, fields, models
from pkg_resources import require

from server.odoo.fields import Many2one


class ActivityPlan(models.Model):
    _name="activity_plan"
    # _Description="Activity Plan"

    # active=fields.Boolean(string="Active")
    company_id = fields.Many2one('res.company',string="Company")
    steps_count=fields.Integer(string="Steps_Count")
    name=fields.Char(string="Name",required=1,default='e.g.Onboarding')
    res_model=fields.Selection([('sales_order','Sales Order')],string="Model",default='sales_order',required=1)
    res_model_id = fields.Char(string="Applies to",required=1)
    # res_model_id=fields.many2one(' ir.model',string="Applies to",)
    template_ids=fields.One2many('activity_plan_template','plan_id',string='Activities')



class ActivityPlanTemplate(models.Model):
    _name="activity_plan_template"


    plan_id=fields.Many2one('activity_plan')
    # activity_type_id=fields.Many2one('activity_type',string='Activity Type',required=1)
    activity_type_id = fields.Selection([('to_do','To DO')], string='Activity Type', required=1)
    summary=fields.Char(string='Summary')
    responsible_type=fields.Selection([('on_demand','Ask at lunch'),
                                       ('other','Default user'),
                                       ('coach','Coach'),
                                       ('manger','Manger'),
                                       ('employee','Employee')],
                                      string='Assignment',default='on_demand',required=1)
    responsible_id=fields.Many2one('res.users',string='Assigned to ')
    delay_count=fields.Integer(string='interval')
    delay_unit=fields.Selection([('days','days'),
                                ('weeks','weeks'),
                                ('months','months')],
                                string='Units',default='days',required=1)
    delay_from=fields.Selection([('before_pan_date','Before Plan Date'),
                                 ('after_pan_date','After Plan Date'),],
                                string='Trigger',default='before_pan_date',required=1)