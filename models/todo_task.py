from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    #Fields
    task_name = fields.Char(string="Task Name", required=True, tracking=1)
    description = fields.Char(string="Description")
    due_date = fields.Date(string="Due Date")
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='new')

    #Relations
    assign_to = fields.Many2one('res.partner', required=True, tracking=1)

    #Action Methods
    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'