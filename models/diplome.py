# -*- coding: utf-8 -*-

from odoo import models, fields

class Diplomes(models.Model):
    _name = "gestion.clinique.diplome"
    _description = "Diplome"


    name = fields.Char(string="Intitule", required=True)
    niveau = fields.Selection([('1','Intermediaire'),('2','Professionnel'),('3','Expert')],string="Niveau",required=True)
    medecin_ids=fields.Many2many('gestion.clinique.docteur',string="medecin")
    