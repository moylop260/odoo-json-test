# -*- coding: utf-8 -*-
##############################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    license: http://www.gnu.org/licenses/agpl-3.0.html
#    info Vauxoo (info@vauxoo.com)
#    coded by: moylop260@vauxoo.com
#    planned by: nhomar@vauxoo.com
#                moylop260@vauxoo.com
############################################################################

import json
import requests

from openerp.tests.common import HttpCase
from openerp import tools


HOST = '127.0.0.1'
PORT = tools.config['xmlrpc_port']


class TestJsonPost(HttpCase):
    def setUp(self):
        super(TestJsonPost, self).setUp()
        self.url_base = "http://%s:%s" % (HOST, PORT)
        self.url = self.get_url()

    def get_url(self, url='/json_provider_test'):
        """
        :param string url: Last url to use.
            default: /json_provider_test
        :return: url full url plus session id
        http://IP:PORT/json_provider_test?session_id=###
        """
        if url.startswith('/'):
            url = self.url_base + url
        url += '?session_id=' + self.session_id
        return url

    def post_json(self, url, data,
                  headers=None, params=None):
        """
        :param string url: Full url of webhook services.
        :param dict data: Payload data of request.
        :param dict headers: Request headers with main data.
        :param dict params: Extra values to send to json.
        """
        if headers is None:
            headers = {}
        headers.update({
            'X-Json-Test-Event': 'test-json',
            'X-Json-Test-Address': HOST,
        })
        headers.setdefault('accept', 'application/json')
        headers.setdefault('content-type', 'application/json')
        payload = json.dumps(data)
        response = requests.request(
            "POST", url, data=payload,
            headers=headers, params=params)
        return response.json()

    def test_post_json_data(self):
        """
        Test to check that post json data is sended done!
        """
        json_response = self.post_json(
            self.url, {'foo': 'bar'})
        self.assertEqual(
            json_response.get('error', False), False,
            'Error in json post data!.')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
