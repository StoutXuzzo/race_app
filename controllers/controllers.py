# -*- coding: utf-8 -*-
# from odoo import http


# class RaceApp(http.Controller):
#     @http.route('/race_app/race_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/race_app/race_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('race_app.listing', {
#             'root': '/race_app/race_app',
#             'objects': http.request.env['race_app.race_app'].search([]),
#         })

#     @http.route('/race_app/race_app/objects/<model("race_app.race_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('race_app.object', {
#             'object': obj
#         })
