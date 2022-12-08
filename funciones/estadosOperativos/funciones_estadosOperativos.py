from flask import render_template, redirect, request
from data_base import database as mongodb
from forms.ESTADOOPERATIVO.estado import EstadosCat
import random

DB = mongodb.dbConecction()

def EstadosOperativos():
    titulo="Base de datos estados operativos"
    EstadosDB = DB['estadoscat']
    EstadosRecividos = EstadosDB.find()
    return render_template('/ADMINISTRADOR/estados_operativos/base_datos.html',titulo=titulo,EstadosRecividos=EstadosRecividos)

def NuevoEstado():
    EstadoDB =  DB['estadoscat']
    CategoriaEstado = request.form['EstadoOperativo']
    identificador = str(random.randint(0,2000))

    if identificador and CategoriaEstado:
        categoria = EstadosCat(identificador,CategoriaEstado)     
        EstadoDB.insert_one(categoria.datosEstadoOperativoJson())
        return redirect('/BASE-DATOS-ESTADOS-OPERATIVOS')

def EliminarEstado(key):
    EstadoDB = DB['estadoscat']
    EstadoDB.delete_one({'identificador':key})   
    return redirect('/BASE-DATOS-ESTADOS-OPERATIVOS')            