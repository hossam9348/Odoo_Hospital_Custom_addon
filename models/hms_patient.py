from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date
import re


class HMSPatient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    email = fields.Char()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([('A+','A+') , ('O+','O+')])
    PCR = fields.Boolean()
    img = fields.Image()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age' , store=True)
    status = fields.Selection([('Undetermined' ,'Undetermined' )  , ('Good' , 'Good')  , ('Fair' , 'Fair'), ('Serious' , 'Serious')] ,default = 'Undetermined')

    doctors_ids = fields.Many2many('hms.doctor')
    department_id = fields.Many2one('hms.department')

    department_capacity = fields.Integer(related = 'department_id.capacity')

    patient_log_status = fields.One2many('hms.patient.log' , 'patient_id')


    @api.onchange('status')
    def status_log(self):
        vals = {
            'description': 'status Changed to %s'%(self.status) ,
             'patient_id': self.id
        }

        self.env['hms.patient.log'].create(vals)

    @api.onchange('age')
    def age_pcr_relation(self):
        if self.age:
           if self.age < 30 and self.PCR == False :
            self.PCR = True
            return{
            'warning' : {
                'title': ('PCR Checked Warning') ,
                'message': 'PCR Checked !'}
            }

    @api.constrains('email')
    def check_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if self.email == False:
            raise ValidationError('emial must be valid')
        elif not re.fullmatch(regex, self.email):
            raise ValidationError('emial must be valid')
   

        
    _sql_constraints =[
        ('email_unique' , 'UNIQUE(email)' , 'emial must be unique'),
    ]

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date :
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else :
                rec.age= 0



  



