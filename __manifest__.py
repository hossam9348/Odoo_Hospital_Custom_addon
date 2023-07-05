{
    'name': 'HMS',
    'author':'Hosssam',
    'description': 'an Application for a hospital',
    'version' : '0.1',
    'depends' : ['crm'],
    'data':[
    'security/ir.model.access.csv',
    'security/res_groups.xml',
    'views/hms_patient_view.xml',
    'views/hms_doctor_view.xml',
    'views/hms_department_view.xml',
    'views/hms_customer_template_inheirt_view.xml',
    'reports/hms_patient_template.xml',
    'reports/reports.xml'
    ]
}