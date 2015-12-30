from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone

class home_mode(models.Model):
    _name = 'home.mode'

    name = fields.Char(string="Name", required=True)
    home_id = fields.Many2one('home.home', string="Home", required=True)
    methods = fields.Many2many('home.appliance.method', string="Methods")