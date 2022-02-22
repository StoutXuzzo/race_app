# -*- coding: utf-8 -*-

from operator import index
import re
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class PilotModel(models.Model):
    _name = 'race_app.pilot_model'
    _description = 'Pilot Model'
    _sql_constraints = [('pilot_unique_dni', 'UNIQUE(dni)', 'The DNI must be unique.'),
    ('pilot_unique_id', 'UNIQUE(id)', 'This ID already exist.'),
    ('pilot_unique_name_surname', 'UNIQUE(name, surname)', 'This pilot is already registred.'),]

    id = fields.Integer("ID: ", default = lambda self: self.getId(), required=True, help="Pilot ID.")
    dni = fields.Char("DNI: ", required=True, index=True, help="Pilot DNI.")
    name = fields.Char("Name: ", required=True, index=True, help="Pilot name.")
    surname = fields.Char("Surname: ", required=True, index=True, help="Pilot surnames.")
    gender = fields.Selection(string = "Gender: ", selection=[('m','Male'),('f','Female'),('o','Other')])
    photo = fields.Binary("Photo: ", help="Pilot photo.")
    phone = fields.Char("Phone: ", index=True, help="Pilot phone.")
    email = fields.Char("Email: ", index=True, help="Pilot email.", required=True)
    winNum = fields.Integer("Number of wins: ", compute="countWins", store=True)
    noWin = fields.Selection(selection=[('s','s'),('n','n')], default='n', store=True)

    team_id = fields.Many2one('race_app.team_model', "Team: ")
    race_ids = fields.One2many('race_app.race_model', 'pilot_id', 'Winned races: ')
    piloted_ids = fields.One2many('race_app.piloted_model', 'pilot_id', "Race history: ")
    
    def getId(self):
        if len(self.env["race_app.pilot_model"].search([])) > 0:
            return self.env["race_app.pilot_model"].search([])[-1].id + 1
        return 1

    @api.constrains('dni')
    def valDni(self):
        code = "TRWAGMYFPDXBNIZSQVHLCKE"
        dni = self.dni
        dniNum = dni[:-1]
        if dni[:-1].isdigit() and len(dni) == 9:
            dniNum = int(dniNum)
            num = dniNum % 23
            if dni[-1] == code[num]:
                return dni
            else:
                raise ValidationError('The DNI is not correct.')
        else:
            raise ValidationError('The DNI is not correct.')

    @api.constrains('email')
    def valEmail(self):
        email = self.email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            raise ValidationError('The email is not correct.')

    @api.depends('race_ids')
    def countWins(self):
        self.winNum = len(self.race_ids)
        if self.winNum > 0:
            self.noWin = 's'
        else:
            self.noWin = 'n'

