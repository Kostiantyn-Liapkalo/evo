from odoo import models, fields

class HrJob(models.Model):
    _inherit = 'hr.job'

    working_hours_per_week = fields.Float(string='Working Hours per Week', default=40.0)