from odoo import api, fields, models, _


class PatientAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Appointment class'

    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: _('New'))
    patient_name = fields.Many2one('patients.details', 'Patient Name')
    age = fields.Integer(related='patient_name.age', string='Age')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M', related='patient_name.gender',
                              string='Gender')
    date = fields.Date('Date')
    date_time = fields.Datetime('Appointment Time')
    doctor_name = fields.Many2one('doctors.details', 'Doctor Name')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.appointment') or _('New')
        return super(PatientAppointment, self).create(vals)

    @api.onchange('patient_name')
    def onchange_patient_name(self):
        if self.patient_name:
            if self.patient_name.doctors_id:
                self.doctor_name = self.patient_name.doctors_id
