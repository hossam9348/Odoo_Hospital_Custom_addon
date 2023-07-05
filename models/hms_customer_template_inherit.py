from odoo import fields, models, api
from odoo.exceptions import ValidationError
import logging




class CustomerTemplateInherit(models.Model):
    _logger = logging.getLogger(__name__)
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one('hms.patient')
    vat = fields.Char(required = True)

    @api.constrains('related_patient_id')
    def one2one(self):
      if self.related_patient_id  != False: 
        customersWithPatients = self.search([('related_patient_id', '!=', False)])
        _logger.debug('*******************************************************************')
        _logger.debug(customersWithPatients)
        print(customersWithPatients)
        for customer in customersWithPatients:
            if self.related_patient_id.email == customer.related_patient_id.email:
                 raise ValidationError('customer must be assigned to only one patient')
    
