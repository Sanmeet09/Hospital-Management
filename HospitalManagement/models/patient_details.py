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
    appointment_count = fields.Integer('Appointment Count', compute='compute_appointment_count')

    def compute_appointment_count(self):
        appointment_count = self.env['patient.appointment'].search_count([('patient_name', '=', self.id)])
        self.appointment_count = appointment_count

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

    # def write(self, vals):
    #     patient_name = self.patient_name
    #     if 'Mr ' or 'Mrs ' in patient_name:
    #         if 'Mr ' or 'Mrs ':
    #             patient_name.replace('Mr ', ' ')
    #         else:
    #             patient_name.replace('Mrs ', ' ')
    #     if vals.get('gender') == 'M':
    #         self.patient_name = "Mr " + self.patient_name
    #     elif vals.get('gender') == 'F':
    #         self.patient_name = "Mrs " + self.patient_name
    #
    #     else:
    #         self.patient_name = ''
    #     res = super(PatientsDetails, self).write(vals)
    #     return res

    # @api.onchange('gender')
    # def calculate_gender(self):
    #     for rec in self:
    #         if rec.gender == 'M':
    #             if "Mrs" in rec.patient_name:
    #                 rec.patient_name = rec.patient_name.replace("Mrs", "Mr")
    #             else:
    #                 rec.patient_name = 'Mr ' + rec.patient_name
    #         elif rec.gender == 'F':
    #             if "Mr" in rec.patient_name:
    #                 rec.patient_name = rec.patient_name.replace("Mr", "Mrs")
    #             else:
    #                 rec.patient_name = 'Mrs ' + rec.patient_name
    #         elif rec.gender == False:
    #             if "Mr " in rec.patient_name:
    #                 rec.patient_name = rec.patient_name.lstrip("Mr")
    #             elif "Mrs " in rec.patient_name:
    #                 rec.patient_name = rec.patient_name.lstrip("Mrs")

    @api.onchange('gender')
    def check_gender(self):
        for rec in self:
            name = rec.patient_name
            if rec.patient_name:
                if "Mr " in rec.patient_name:
                    rec.patient_name = name.lstrip("Mr ")
                elif "Mrs " in rec.patient_name:
                    rec.patient_name = name.lstrip("Mrs ")
                else:
                    rec.patient_name = name
                if rec.gender == 'M':
                    rec.patient_name = "Mr " + rec.patient_name
                elif rec.gender == 'F':
                    rec.patient_name = "Mrs " + rec.patient_name
                else:
                    rec.patient_name = rec.patient_name

    # @api.onchange('gender')
    # def editing_value(self):
    #     for rec in self:
    #         if rec.patient_name:
    #             if rec.gender == 'M':
    #                 name = rec.patient_name
    #                 if 'Mr ' or 'Mrs ' in rec.patient_name:
    #                     name.replace('mrs ', ' ')
    #                     print("after lstrip", name)
    #                     rec.prefix = 'mr'
    #                     full_name = rec.prefix + ' ' + name
    #                     rec.patient_name = full_name
    #                 else:
    #                     rec.prefix = 'mr'
    #                     full_name = rec.prefix + ' ' + name
    #                     rec.patient_name = full_name
    #             elif rec.gender == 'F':
    #                 name = rec.patient_name
    #                 if 'Mr ' or 'Mrs ' in rec.patient_name:
    #                     name.replace('mr ', ' ')
    #                     rec.prefix = 'mrs'
    #                     full_name = rec.prefix + ' ' + name
    #                     rec.patient_name = full_name
    #                 else:
    #                     rec.prefix = 'mrs'
    #                     full_name = rec.prefix + ' ' + name
    #                     rec.patient_name = full_name
    #             else:
    #                 rec.patient_name = rec.patient_name

    def action_confirm(self):
        pass
