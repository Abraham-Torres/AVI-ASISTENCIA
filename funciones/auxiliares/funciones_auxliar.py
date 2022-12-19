from flask import render_template, request, redirect, session
from data_base import database as mongodb
import random
from forms.AUXILIAR.auxiliar import Auxiliar

DB =mongodb.dbConecction()


def Formulario_Aux():
        titulo = "Nuevo auxiliar"
        auxiliar = DB ['auxiliar']
        auxiliarRecibidos = auxiliar.find()
        return render_template('ADMINISTRADOR/auxliar/registrar.html',titulo=titulo, aux = auxiliarRecibidos)

def Nuevo_Aux():
        if 'usuario-administrador' in session:
                nombre = request.form['nombre']
                correo = request.form['correo']
                edad = request.form['edad']
                telefono = request.form['telefono']
                identificador = str(random.randint(0,2000))+correo

                if nombre and correo and edad and telefono:
                        auxiliares = DB ['auxiliar']
                        auxiliar = Auxiliar(identificador,nombre, correo, edad, telefono)
                        auxiliares.insert_one(auxiliar.datoAuxiliarJson())
                        return redirect('/BASE-DATOS-AUXILIAR')

        elif 'usuario-empleado' in session:
                return redirect('/INICIAR-SESION-EMPLEADO')    

def AuxiliarDb():
        if 'usuario-administrador' in session:
                titulo = "Base de datos auxiliar"
                auxiliares = DB['auxiliar']
                auxiliarRecibidos = auxiliares.find()
                return render_template('/ADMINISTRADOR/auxliar/base_datos.html',titulo=titulo,auxiliar=auxiliarRecibidos)

        elif 'usuario-empleado' in session:
                return redirect('/INICIAR-SESION-EMPLEADO')                                   

def Operaciones_Auxiliar():
        if 'usuario-administrador' in session:
                titulo = "Operaciones auxiliar"
                auxiliares = DB['auxiliar']
                auxiliaresRecibidos = auxiliares.find()
                return render_template('ADMINISTRADOR/auxliar/operaciones.html',titulo=titulo, auxiliar=auxiliaresRecibidos)

        elif 'usuario-empleado' in session:
                return redirect('/INICIAR-SESION-EMPLEADO')  

def Eliminar_Aux(key):
        auxiliares = DB['auxiliar']
        auxiliares.delete_one({'identificador':key})
        return redirect('/OPERACIONES-AUXILIAR')

def Informacion_Aux(key):
        titulo = "Informacion auxiliar"
        auxiliares = DB ['auxiliar']
        auxiliarRecibido = auxiliares.find_one({'identificador':key})
        return render_template('/ADMINISTRADOR/auxliar/informacion.html',titulo=titulo,auxiliares=auxiliarRecibido)

def Actualizar_Aux(key,campo):
        auxiliares = DB['auxiliar']
        dato = request.form['dato']
        if dato:
                auxiliares.update_one({'identificador':key}, {'$set':{campo:dato}})
                return Informacion_Aux(key)