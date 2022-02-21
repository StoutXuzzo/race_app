
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class PilotedModel(models.Model):
    _name = 'race_app.piloted_model'
    _description = 'Piloted Model'

    car_id = fields.Many2one('race_app.car_model', 'Car: ')
    pilot_id = fields.Many2one('race_app.pilot_model', 'Pilot: ')

    race_ids = fields.Many2many('race_app.race_model', string='Races: ')

    @api.onchange('pilot_id')
    def filterWiner(self):
        domain = {'car_id':[('team_id', '=', self.pilot_id.team_id.id)]}
        return {'domain': domain}