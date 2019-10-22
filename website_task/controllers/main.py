# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_portal.controllers.main import website_account



class WebsiteForm(WebsiteForm):

    # Check and insert values from the form on the model <model>
    @http.route('/website_form/<string:model_name>', type='http', auth="user", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        if model_name == 'project.task' and not request.params.get('state'):
            pass
        return super(WebsiteForm, self).website_form(model_name, **kwargs)

    @http.route(['/task/new'], type='http', auth="user", website=True)
    def task(self, country=None, department=None, office_id=None, **kwargs):
        env = request.env(
            context=dict(
                request.env.context, show_address=True, no_tag_br=True)
        )

        projects = request.env['project.project'].search([('privacy_visibility', '=', 'portal')])

        # Render page
        return request.render("website_task.new-task", {"project_filters": projects})

    # Redirect to success page
    @http.route("/task-thank-you", type="http", auth="user", website=True)
    def task_tank_you(self, **kw):
        return request.render("website_task.task-thank-you")
