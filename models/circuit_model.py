# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CircuitModel(models.Model):
    _name = 'race_app.circuit_model'
    _description = 'race_app.race_app'

    name = fields.Char("Name: ", help="Circuit name.", required=True, index=True)
    photo = fields.Binary("Photo: ", help="Circuit photo.")
    km = fields.Float("Km: ", help="Circuit distance.", required=True)
    floor = fields.Selection(string="Floor type: ", selection=[('a','Asphalt'), ('g','Grave'), ('s', 'Soil'), ('m', 'Mixed')], required=True, default='a')
    routeType = fields.Selection(string="Type of route: ", selection=[('c', 'Circuit'), ('s', 'Section')], required=True)