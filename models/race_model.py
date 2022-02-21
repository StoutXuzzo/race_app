# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class RaceModel(models.Model):
    _name = 'race_app.race_model'
    _description = 'Race Model'

    date = fields.Date("Date: ", help="Date of the race", required=True)
    state = fields.Selection(string="State: ", selection=[('p', 'Pending'),('f', 'Finished')], default="p")

    piloted_ids = fields.Many2many('race_app.piloted_model', string='Pilots: ')
    pilot_id = fields.Many2one('race_app.pilot_model', string='Winner: ', default=None)
    circuit_id = fields.Many2one('race_app.circuit_model', string='Circuit: ')

    def finish(self):
        if len(self.pilot_id) > 0:
            self.state = "f"
        else:
            raise ValidationError('You have to select a winner.')
    
    @api.onchange('piloted_ids', 'pilot_id')
    def filterWiner(self):
        domain = {'pilot_id':[]}
        ids = []
        for piloted in self.piloted_ids:
            ids.append(piloted.pilot_id.id)
        domain['pilot_id'].append(('id', '=', ids))
        return {'domain': domain}

    @api.onchange('piloted_ids')
    def filterRacers(self):
        domain = {}
        idp = []
        for piloted in self.piloted_ids:
            idp.append(piloted.pilot_id.id)
        domain['piloted_ids'] = [('pilot_id', '!=', idp)]

        ids = []
        for piloted in self.piloted_ids:
            ids.append(piloted.car_id.id)
        domain['piloted_ids'].append(('car_id', '!=', ids))

        return {'domain': domain}