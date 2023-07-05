from odoo import fields, models




class HMSPatientLog(models.Model):
    _name = 'hms.patient.log'


    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')



