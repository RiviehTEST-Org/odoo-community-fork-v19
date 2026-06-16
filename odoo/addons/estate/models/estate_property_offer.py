# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offers"

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'),('refused', 'Refused')],
        copy=False)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    bidder_id = fields.Many2one("res.partner", string="Bidder", index=True, required=True)