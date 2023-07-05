from odoo import fields , models


class HMSDepartment(models.Model):
    _name = 'hms.department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    # patients = fields.Html()
    
    patients_ids = fields.One2many('hms.patient', 'department_id')
