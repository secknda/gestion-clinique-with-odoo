# -*- coding: utf-8 -*-

from odoo import models, fields

class Grades(models.Model):
    _name = "gestion.clinique.grade"
    _description = "Grades"


    name = fields.Char(string="Nom de la Grdes", required=True)
    code = fields.Char(string="Code de la Grdes", required=True)

