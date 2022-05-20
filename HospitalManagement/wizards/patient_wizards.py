from odoo import fields, api, models, _


class PatientWizard(models.TransientModel):
    _name = 'wizard.patient'
    _description = 'Creating a wizard in patient'

    patient_name = fields.Char('Patient Name')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M', string='Gender')
    description = fields.Char('Description')
    phone_no = fields.Char('Phone No', size=10)
    doctors_id = fields.Many2one('doctors.details', 'Doctor Name')

    @api.model
    def default_get(self, fields):
        res = super(PatientWizard, self).default_get(fields)
        active_model = self.env.context.get('active_id')
        patient_id = self.env['patients.details'].search([('id', '=', active_model)])
        res.update({
            'patient_name': patient_id.patient_name,
            'age': patient_id.age,
            'gender': patient_id.gender,
            'description': patient_id.description,
            'phone_no': patient_id.phone_no,
            'doctors_id': patient_id.doctors_id.id
        })
        return res

    def change_profile(self):
        active_model = self.env.context.get('active_id')
        patient_id = self.env['patients.details'].search([('id', '=', active_model)])
        patient_id.update({
            'patient_name': self.patient_name,
            'age': self.age,
            'gender': self.gender,
            'description': self.description,
            'phone_no': self.phone_no,
            'doctors_id': self.doctors_id.id
        })
