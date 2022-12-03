# -*- coding: utf-8 -*-

from odoo import models, fields

class PersonnelMedical(models.Model):
    _name = "gestion.clinique.docteur"
    _description = "Personnel Médical"


    name = fields.Char(string="Nom et Prénoms", required=True)
    age = fields.Integer(string="Age")
    sexe = fields.Selection([('homme','Masculin'),('femme','Féminin'),('other','Autre')], string="Sexe", required=False,)
    situation_matrimoniale = fields.Selection([('m','Marié'),('c','Célibataire'),('v','Veuve'),('d','Divorcé')], 
        string="Situation Matrimoniale", required=False,)
    domaine_id = fields.Many2one('gestion.clinique.domaine', string="Spécialité")
    grade_id = fields.Many2one('gestion.clinique.grade', string="Grade")
    patient_ids=fields.One2many('gestion.clinique.patient','medecin_id',string="Liste des Patients")
    diplomes_ids=fields.Many2many('gestion.clinique.diplome',string="Diplomes")
    # date_obtenu=fields.Date(string="Date d'obtention",)
    nbr_patient=fields.Char(string="Nombre de Patients",compute='_compute_nbr_patient')


    def _compute_nbr_patient(self):
        self.nbr_patient = len(self.patient_ids)
