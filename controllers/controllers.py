# -*- coding: utf-8 -*-
# from odoo import http


# class SteveWebsiteExtension(http.Controller):
#     @http.route('/steve_website_extension/steve_website_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/steve_website_extension/steve_website_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('steve_website_extension.listing', {
#             'root': '/steve_website_extension/steve_website_extension',
#             'objects': http.request.env['steve_website_extension.steve_website_extension'].search([]),
#         })

#     @http.route('/steve_website_extension/steve_website_extension/objects/<model("steve_website_extension.steve_website_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('steve_website_extension.object', {
#             'object': obj
#         })
