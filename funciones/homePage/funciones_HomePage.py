from flask import render_template
from data_base import database as mongodb

DB = mongodb.dbConecction()

def Home():
    titulo="Inicio"
    operadores = DB['puestos']
    auxiliares = DB['auxiliar']
    auxiliaresTot = auxiliares.count_documents({})
    operadoresTot = operadores.count_documents({})
    print(operadoresTot)
    print(auxiliaresTot)
    return render_template('/index.html',titulo=titulo, Operadores=operadoresTot, Auxiliares= auxiliaresTot)

  

    