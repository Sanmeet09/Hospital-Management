from odoo import models, api, fields, _


class PatientsDetails(models.Model):
    _name = 'patients.details'
    _rec_name = 'patient_name'
    _description = 'Details of all the patient on the first page'

    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: _('New'))
    patient_name = fields.Char('Patient Name')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M', string='Gender')
    description = fields.Char('Description')
    phone_no = fields.Char('Phone No', size=10)
    doctors_id = fields.Many2one('doctors.details', 'Doctor Name')

    # This Function is used to create the sequence for the patient
    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patients.details') or _('New')
        if vals.get('gender') == 'M':
            vals['patient_name'] = 'Mr ' + vals['patient_name']
        else:
            vals['patient_name'] = 'Mrs ' + vals['patient_name']
        return super(PatientsDetails, self).create(vals)


    # def write(self,vals):
    #     if self.patient_name == 'M':
    #         self['patient_name'] = 'Mr ' + self['patient_name']
    #     elif self.patient_name == 'F':
    #         self['patient_name'] = 'Mrs ' + self['patient_name']
    #     else:
    #         self['patient_name'] = 'none'
    #     return super(PatientsDetails,self).write(vals)


    # def write(self,vals):
    #     if self['gender'] == 'M':
    #         self['patient_name'] = 'Mr ' + self['patient_name']
    #     else:
    #         self['patient_name'] = 'Mrs ' + self['patient_name']
    #     return super(PatientsDetails, self).write(vals)


