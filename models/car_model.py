# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random


class CarModel(models.Model):
    _name = 'race_app.car_model'
    _description = 'Car Model'
    _sql_constrain = [('car_unique_number', 'UNIQUE(number)', 'This number is on another car.')]

    name = fields.Char("Name: ", compute="getName", store=True)
    number = fields.Integer("Number: ", help="Car number.", index=True)
    photo = fields.Binary("Photo: ", help="Car photo.")
    brand = fields.Char(string="Brand: ", help="Car brand.", required=True)
    model = fields.Char(string="Model: ", help="Car model.", required=True)
    year = fields.Integer(string="Year: ", help="Model year.", required=True)
    hp = fields.Integer(string="Horse Power: ", help="Car HP.", required=True)
    zeroToOneHundred = fields.Float(string="0/100 km/h", help="Car acceleration.")
    traction = fields.Selection(string="Traction: ", selection=[('f', 'FWD'), ('r', 'RWD'), ('a', 'AWD')], help="Type of traction.", required=True)
    fuel = fields.Selection(string="Fuel type: ", selection=[('g', 'Gasoline'), ('d','Diesel'), ('h', 'Hybrid'), ('e', 'Electric')], help="Type of fuel.", required=True)

    team_id = fields.Many2one('race_app.team_model', string="Team owner: ")

    @api.depends('number', 'brand', 'year')
    def getName(self):
        for r in self:
            r.name = r.brand + " - " + r.model + " - " + str(r.year)
        return True

    @api.depends('hp')
    def randomNumber(self):
        number = random.randint(0, 9999) + self.hp

        for elem in self.env["race_app.car_model"].search([]):
            if elem.number == number:
                self.randomNumber()
            else:
                self.number = number
                return True