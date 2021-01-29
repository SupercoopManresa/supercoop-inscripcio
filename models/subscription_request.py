# -*- coding: utf-8 -*-
from odoo import fields, models, _


class SubscriptionRequest(models.Model):
    _inherit = 'subscription.request'

    discovery_channel = fields.Selection(
        selection = [
            ('boca', _('Boca-orella')),
            ('fulleto', _('Fulletó')),
            ('radio', _('Ràdio')),
            ('tv', _('TV')),
            ('premsa', _('Premsa')),
            ('xarxes', _('Xarxes socials')),
            ('web', _('WEB')),
            ('buscador', _('Buscador d’internet')),
            ('socia', _('Sòcia ecoopirativa/estrella')),
            ('altres', _('Altres'))
        ],
        help = 'How people find us.',
        string = 'Discovery channel'
    )
    newsletter_approved = fields.Boolean(
        string='Newsletter approved',
        required=True,
        default=False,
    )
   

    def get_required_field(self):
        req_fields = super(SubscriptionRequest, self).get_required_field()
        req_fields.append('discovery_channel')

        return req_fields
