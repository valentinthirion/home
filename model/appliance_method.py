from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone

class appliance_method(models.Model):
    _name = 'home.appliance.method'

    name = fields.Char(string="Name", required=True)
    appliance_id = fields.Many2one('home.appliance', string="Appliance", required=True)

    description = fields.Text(string="Description")
    url = fields.Char(string="URL")

    last_executed = fields.Datetime(string="Last executed")

