from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'task_name'

    #Fields
    task_name = fields.Char(string="Task Name", required=True, tracking=1)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date", required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ], default='new')

    estimated_time = fields.Float(string="Estimated Time (in hours)", required=True)

    total_timesheet_time = fields.Float(compute='_compute_total_timesheet_time', string="Total Timesheet Time (in hours)")

    #Field to track due_date field
    is_late = fields.Boolean(string="Late", default=False)

    # Archiving field
    active = fields.Boolean(default=True)

    #Relations
    assign_to_id = fields.Many2one('res.partner', required=True, tracking=1)

    line_ids = fields.One2many('timesheet', 'todo_task_id', string="Timesheet")

    #Window Action Methods
    def action_new(self):
        for rec in self:
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'

    #Compute Methods
    @api.depends('line_ids')
    def _compute_total_timesheet_time(self):
        for rec in self:
            rec.total_timesheet_time = 0
            for line in rec.line_ids:
                rec.total_timesheet_time = rec.total_timesheet_time + line.time
            if rec.total_timesheet_time > rec.estimated_time:
                raise ValidationError('Total Timesheet time exceeds estimated time!')

    #Server Action Method
    def server_action_closed(self):
        for rec in self:
            rec.status = 'closed'

    #Automated Action (Cron Job)
    def cron_action_check_due_date(self):
        todo_task_ids = self.search([('status', '==', 'in_progress')])
        for rec in todo_task_ids:
            if rec.due_date and rec.due_date < fields.Date.today():
                rec.is_late = True
            else:
                rec.is_late = False

class TodoTaskLine(models.Model):
    _name = 'timesheet'
    _description = 'To-Do Timesheet'

    #Fields
    date = fields.Date(string="Date", required=True)
    description = fields.Text(string="Description", required=True)
    time = fields.Float(string="Time (in hours)", required=True)

    #Relations
    todo_task_id = fields.Many2one('todo.task')