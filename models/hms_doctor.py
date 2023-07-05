from odoo import fields , models


class HMSDoctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    img = fields.Binary()
