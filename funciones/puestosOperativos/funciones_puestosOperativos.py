from flask import render_template, redirect, request
import random
from data_base import database as mongodb
from forms.PUESTOOPERATIVO.puestoOperativo import Operativo

DB = mongodb.dbConecction()


def PuestoOperativoDb():
    titulo = "Base de datos Puestos operativos"
    OperativosDB = DB['operativos']
    DBOperativos = OperativosDB.find()
    return render_template('ADMINISTRADOR/puestos_operativos/base_datos.html',titulo=titulo,Operativos=DBOperativos)

def NuevoPuestoOperativo():
    OperativosDB = DB['operativos']
    PuestoOperativo = request.form['PuestoOperativo']
    identificador = str(random.randint(0,2000))+PuestoOperativo

    if identificador and PuestoOperativo:
        tipo = Operativo(identificador,PuestoOperativo)
        OperativosDB.insert_one(tipo.datosOperativoJson())
        return redirect('/BASE-DATOS-PUESTOS-OPERATIVOS')

def EliminarPuestoOperativo(key):
    OperativosDB = DB['operativos']
    OperativosDB.delete_one({'identificador':key})   
    return redirect('/BASE-DATOS-PUESTOS-OPERATIVOS')
