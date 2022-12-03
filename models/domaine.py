# -*- coding: utf-8 -*-

from odoo import models, fields

class Domaines(models.Model):
    _name = "gestion.clinique.domaine"
    _description = "Spécialités"


    name = fields.Char(string="Nom de la Spécialités", required=True)
    code = fields.Char(string="Code de la Spécialités", required=True)

