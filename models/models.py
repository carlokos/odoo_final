# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


# class escuela(models.Model):
#     _name = 'escuela.escuela'
#     _description = 'escuela.escuela'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class alumno(models.Model):
    _name = 'escuela.alumno'
    _description = 'model alumno'

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    edad = fields.Integer(String="Edad", compute="_get_edad")

    curso_id = fields.One2many('escuela.curso', 'alumnos_id', string="Curso")

    @api.depends('fecha_nacimiento')
    def _get_edad(self):
        for alumno in self:
            hoy = date.today()
            alumno.edad = relativedelta(hoy, alumno.fecha_nacimiento).years

class curso(models.Model):
    _name = 'escuela.curso'
    _description = 'model curso'

    name = fields.Char('ID', required=True)
    nombre = fields.Char('Curso', required=True)

    asignaturas_id = fields.Many2many('escuela.asignatura', string='Asignaturas')
    alumnos_id = fields.Many2one('escuela.alumno', string='Alumnos')

class asingnatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'model asignatura'

    name = fields.Char('ID', required=True)
    nombre = fields.Char('Nombre', required=True)

    cursos_id = fields.Many2many('escuela.curso', string='Curso')