# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError
import string

class Patient(models.Model):
    _name = "gestion.clinique.patient"
    _description = "Liste des patients"


    name = fields.Char(string="Nom de famille", required=True)
    fist_name = fields.Char(string="Prénoms", required=True)
    sexe = fields.Selection([('homme','Masculin'),('femme','Féminin'),('other','Autre')], string="Sexe", required=False,)
    date_naissance = fields.Date(string="Date de Naissance")
    lieu_naissance = fields.Char(string="Lieu de Naissance")
    assurance = fields.Boolean(string="Etes-Vous assuré")
    organisation = fields.Char(string="Societe Assuree", required=False)
    assureur = fields.Char(string="Societe Assureur", required=False)
    prix_ticket = fields.Integer(string="Prix du Ticket", compute='_compute_prix_ticket', store=True)
    pourcentage=fields.Integer(string="Pourcentage %")
    date_admis = fields.Datetime(string="Date d'enregistrement")
    phone = fields.Char(string="Numéro de Téléphone")
    email = fields.Char(string="Email")
    medecin_id=fields.Many2one('gestion.clinique.docteur',string="Liste des Medecins")
    number_dossier= fields.Char(string="Numero de Dossier", required=True, copy=False, readonly=True,index=True,default='New')
    state = fields.Selection([('new','Nouveau'),('transfered','Trnsfere'),('consulted','Consulte'),('rejected','Libere'),('hospitalise','Hospitalise')], 
        string="Statut de Patient", required=False, default='new', tracking=True)

    def action_new(self):
        self.state='new'

    def action_transfered(self):
        self.state='transfered'

    def action_consulted(self):
        self.state='consulted'

    def action_rejected(self):
        self.state='rejected'

    def action_hospitalise(self):
        self.state='hospitalise'

    @api.depends('pourcentage')
    def _compute_prix_ticket(self):
        for record in self:
            if record.assurance==False:
                record.prix_ticket=25000

            else:
                record.prix_ticket=(25000*(100-record.pourcentage))/100


    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('gestion.clinique.patient') or '/'
        vals['number_dossier']=seq
        return super(Patient, self).create(vals)

        