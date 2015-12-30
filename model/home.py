from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone

class home(models.Model):
    _name = 'home.home'

    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address")

    appliances = fields.One2many('home.appliance', 'home_id', string="Appliances")
    groups = fields.One2many('home.appliances.group', 'home_id', string="Groups")