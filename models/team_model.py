# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TeamModel(models.Model):
    _name = 'race_app.team_model'
    _description = 'Team model'
    _sql_constrain = [('team_unique_name', 'UNIQUE(name)', 'The name must be unique.')]

    name = fields.Char("Name: ", help="Team name.", index=True)
    photo = fields.Binary("Photo: ", help="Team logo.")
    pilotNum = fields.Integer("Number of pilots: ", compute="countPilots", store=True)
    carNum = fields.Integer("Number of cars: ", compute="countCars", store=True)

    car_ids = fields.One2many('race_app.car_model', 'team_id', string="Team Cars: ")
    pilot_ids = fields.One2many('race_app.pilot_model', 'team_id', string="Team pilots: ")

    @api.depends('car_ids')
    def countCars(self):
        count = 0
        for a in self.car_ids:
            if a.team_id.name == self.name:
                count += 1
        self.carNum = count


    @api.depends('pilot_ids')
    def countPilots(self):
        count = 0
        for a in self.pilot_ids:
            if a.team_id.name == self.name:
                count += 1
        self.pilotNum = count