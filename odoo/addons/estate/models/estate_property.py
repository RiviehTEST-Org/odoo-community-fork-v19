# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta


class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Properties"

    name = fields.Char('Name of Property', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float('List Price', required=True)
    selling_price = fields.Float('Price Sold', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Specify the direction the garden is facing")
    active = fields.Boolean('Active Listing', default=True)
    states = fields.Selection(
        string='Listing Stage',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        default='new',
        help="The status of the property listing")
