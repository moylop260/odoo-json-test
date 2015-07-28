# -*- coding: utf-8 -*-
##############################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    license: http://www.gnu.org/licenses/agpl-3.0.html
#    info Vauxoo (info@vauxoo.com)
#    coded by: moylop260@vauxoo.com
############################################################################


from openerp.addons.web import http
from openerp.http import request
from openerp import exceptions


class WebhookController(http.Controller):

    @http.route(['/json_provider_test'], type='json',
                auth='none', method=['POST'])
    def json_provider_test(self, **post):
        '''
        :params dict post: All extra parameters of json request
        '''
        if not request.httprequest.data:
            raise exceptions.ValidationError(
                'http request data is empty :('
            )
        return True
