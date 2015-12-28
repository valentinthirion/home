from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone

class appliances_group(models.Model):
    _name = 'home.appliances.group'

    name = fields.Char(string="Name", required=True)
    appliances = fields.Many2many('home.appliance', string="Appliances")

