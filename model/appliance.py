from openerp import models, fields, api
import datetime
from datetime import date
from pytz import timezone
from openerp import tools

class appliance(models.Model):
    _name = 'home.appliance'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", compute="_compute_code", required=True)
    home_id = fields.Many2one('home.home', string="Home", required=True)

    description = fields.Text(string="Description")
    status = fields.Char(string="Status")

    type = fields.Selection([('camera', 'Camera'), ('door', 'Door'), ('lamp', 'Lamp'), ('sensor', 'Sensor'), ('thermostat', 'Thermostat')], string="Type", required=True)
    ip = fields.Char(string="IP Address", required=True)

    image = fields.Binary("Photo", attachment=True)
    image_medium = fields.Binary("Medium-sized photo",
        compute='_compute_images', inverse='_inverse_image_medium', store=True, attachment=True)
    image_small = fields.Binary("Small-sized photo",
        compute='_compute_images', inverse='_inverse_image_small', store=True, attachment=True)

    methods = fields.One2many('home.appliance.method', 'appliance_id', string="Methods")
    groups = fields.Many2many('home.appliances.group', string="Groups")

    @api.one
    @api.onchange('name')
    def _compute_code(self):
        if self.name:
            string = self.name.lower()
            string = string.replace(' ', '')
            self.code = string

    @api.depends('image')
    def _compute_images(self):
        for rec in self:
            rec.image_medium = tools.image_resize_image_medium(rec.image)
            rec.image_small = tools.image_resize_image_small(rec.image)

    def _inverse_image_medium(self):
        for rec in self:
            rec.image = tools.image_resize_image_big(rec.image_medium)

    def _inverse_image_small(self):
        for rec in self:
            rec.image = tools.image_resize_image_big(rec.image_small)


