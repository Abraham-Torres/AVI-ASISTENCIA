from flask import render_template, session, redirect
from data_base import database as mongodb

DB = mongodb.dbConecction()

def Home():
    if 'usuario-administrador' in session:
        titulo="Inicio"
        operadores = DB['puestos']
        auxiliares = DB['auxiliar']
        auxiliaresTot = auxiliares.count_documents({})
        operadoresTot = operadores.count_documents({})
        EmpleadosTot = auxiliaresTot + operadoresTot
        return render_template('/index.html',titulo=titulo, Operadores=operadoresTot, Auxiliares=auxiliaresTot, Empleados=EmpleadosTot)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    

    