from dateutil.relativedelta import relativedelta
from odoo import models, fields


class estate_property(models.Model):
    _name = "estate.property"
    _description = "Property to sale"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=True, default=fields.date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden orientation',
        selection=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='Status',
        selection=[('1', 'New'), ('2', 'Offer Received'), ('3', 'Offer Accepted'), ('4', 'Sold'), ('5', 'Canceled')],
        default='1')
