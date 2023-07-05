from odoo import fields , models , api
from odoo.exceptions import ValidationError
from datetime import date


class ITIStudent(models.Model):
    _name = 'iti.student'
    # _rec_name = 'age'


    name = fields.Char()
    date_birth = fields.Date()
    age = fields.Integer(compute='_compute_age' , store=True)
    graduate_age = fields.Integer(compute='_compute_age' , store = True)
    gender = fields.Selection([('female','f') , ('male','m')])
    salary = fields.Float()

    is_accepted = fields.Boolean()
    level = fields.Selection([('level1' ,'Prep' )  , ('level2' , 'Sec')  , ('level3' , 'Graduate')] ,default = 'level1')
    info = fields.Text()
    cv = fields.Html()
    is_working = fields.Boolean(default = False)
    track_id = fields.Many2one('iti.track')

    track_capacity = fields.Integer(related = 'track_id.capacity')

    track_fees = fields.Float(related = 'track_id.fees')

    student_log_levels = fields.One2many('iti.student.log' , 'student_id')

    _sql_constraints =[
        ('salary_check' , 'CHECK(salary >= 0)' , 'Error Salary Can\'t be Negative Number'),
        ('age_check', 'CHECK(age > 0)', 'Error Age Can\'t be Negative Number or Equal to Zero'),
    ]


    @api.depends('date_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_birth :
                today = date.today()
                rec.age = today.year - rec.date_birth.year - (
                        (today.month, today.day) < (rec.date_birth.month, rec.date_birth.day))
                rec.graduate_age = rec.age + 5
            else :
                rec.age= 1
                rec.graduate_age = 0

    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age <= 0 :
    #             raise ValidationError('Age Can\'t be less than or Equal Zero')

    @api.onchange('is_working')
    def set_level(self):
        if self.level == 'level1':
            self.level = 'level2'
        elif self.level == 'level2':
            self.level = 'level3'

        return {
            'warning': {
                'title': ('Level Change Warning'),
                'message': 'Level is Changed to %s' % (self.level)}
        }

    def is_accepted_changed(self):
        for rec in self :
            rec.is_accepted = True ## rec.write({'is_accepted' : True})


    @api.onchange('track_id')
    def track_updated(self):
        if self.track_id :
            return{
            'warning' : {
                'title': ('Track Change Warning') ,
                'message': 'track is Changed to %s'%(self.track_id)}
            }


    @api.onchange('level')
    def level_log(self):
        vals = {
            'description': 'Level Changed to %s'%(self.level) ,
             'student_id': self.id
        }

        self.env['iti.student.log'].create(vals)
