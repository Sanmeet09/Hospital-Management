from odoo import models, api, fields, _


class PatientsDetails(models.Model):
    _name = 'patients.details'
    _description = 'Details of all the patient on the first page'

    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: _('New'))
    patient_name = fields.Char('Patient Name')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M', string='Gender')
    description = fields.Char('Description')

    # This Function is used to create the sequence for the patient
    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patients.details') or _('New')
        return super(PatientsDetails, self).create(vals)
