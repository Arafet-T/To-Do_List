from odoo import models, fields
from odoo.exceptions import ValidationError


class BulkTaskAssignment(models.TransientModel):
    _name = 'bulk.task.assignment'

    todo_task_ids = fields.Many2many('todo.task', string='Selected Tasks')
    assign_to_id = fields.Many2one('res.partner', required=True)

    def action_wizard_confirm(self):
        for rec in self:
            for task in rec.todo_task_ids:
                if task.status in ('new', 'in_progress') :
                    rec.todo_task_ids.assign_to_id = rec.assign_to_id
                else :
                    raise ValidationError('You cannot assign completed or closed tasks to partners. Only assign new or in progress tasks!')