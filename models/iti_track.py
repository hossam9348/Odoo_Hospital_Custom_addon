from odoo import fields , models


class ITITrack(models.Model):
    _name = 'iti.track'



    name = fields.Char()
    capacity = fields.Integer()

    description = fields.Text()

    fees = fields.Float()
    is_opened = fields.Boolean(default = False)

    student_ids = fields.One2many('iti.student' , 'track_id')