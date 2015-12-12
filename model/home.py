from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone

class home(models.Model):
    _name = 'home'

    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address")