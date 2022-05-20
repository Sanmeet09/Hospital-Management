from odoo import api,fields,models, _


class DoctorsDetails(models.Model):
    _name = 'doctors.details'
    _rec_name = 'doctors_name'
    _description = 'Details of all the doctors'


    doctors_name = fields.Char('Doctor\'s Name')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M', string='Gender')
    description = fields.Char('Description')
    doctor_appointment = fields.Date('Date')
    doctors_ids = fields.One2many('doctors.details.line','doctors_id', 'doctor id')

    def create_patients(self):
        patient_id = self.env['patients.details'].create({
            'patient_name':'Sawan',
            'age': self.age,
            'gender':'M',
            'doctors_id': self.id
        })
        print(patient_id)


class DoctorsDetailsLine(models.Model):
    _name = 'doctors.details.line'
    _description = 'One2many field in doctors'

    doctors_id = fields.Many2one('doctors.details','doctor ids')

    patient_name = fields.Many2one('patients.details','Patient Name')
    name = fields.Char(related='patient_name.name',string='Name')
    age = fields.Integer(related='patient_name.age', string='Age')
    gender = fields.Selection(related='patient_name.gender', string='Gender')
    description = fields.Char('Description')





# inheriting phone no

class InheritInDoctorsDetails(models.Model):
    _inherit = 'doctors.details'
    _description = 'Inherit In doctors'

    phone_no = fields.Char('Phone No', size=10)