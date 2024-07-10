from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    work_address_id = fields.Many2one('res.partner', string='Work Address')
    tz = fields.Selection(related='resource_id.tz', string='Timezone', readonly=False)
    pension_fund_tax = fields.Boolean(string='Pension Fund Tax')


    department_id = fields.Many2one('hr.department', string='Department', groups="base.group_user", invisible=True)
    job_id = fields.Many2one('hr.job', string='Job Position', groups="base.group_user", invisible=True)
    parent_id = fields.Many2one('hr.employee', string='Manager', groups="base.group_user", invisible=True)
    coach_id = fields.Many2one('hr.employee', string='Coach', groups="base.group_user", invisible=True)

    position_ids = fields.One2many('employee.position', 'employee_id', string='Positions')


    vacation_days_total = fields.Integer(string='Total Vacation, days', readonly=True)
    vacation_days_used = fields.Integer(string='Used Vacation, days', readonly=True)
    vacation_days_rest = fields.Integer(string='Rest of Vacation, days', readonly=True)
    note = fields.Text(string='Note')

   
    child_ids = fields.One2many('hr.employee', 'parent_id', string='Direct Subordinates')
