from flask import render_template, request, redirect, session
from data_base import database as mongodb
from forms.PUESTO.puesto import Puesto
import random
from werkzeug.security import generate_password_hash, check_password_hash

DB = mongodb.dbConecction()

def PuestoDb():
    if 'usuario-administrador' in session:
        titulo="Base de datos puesto"
        puestos= DB ['puestos']
        puestosRecibidos=puestos.find()
        return render_template('ADMINISTRADOR/puestos/base_datos.html',titulo=titulo,puesto=puestosRecibidos)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
def Formulario():
        titulo="Nuevo puesto"
        OperativosDB=DB['operativos']
        OperativosRecibidos=OperativosDB.find()
        return render_template('ADMINISTRADOR/puestos/registrar.html', titulo=titulo,op=OperativosRecibidos)
       
def Nuevo():
    if 'usuario-administrador' in session:
        nombre=request.form['nombre']
        correo=request.form['correo']
        edad=request.form['edad']
        telefono=request.form['telefono']
        tipo_puesto=request.form['tipo_puesto']
        password=request.form['password']
        activo = False
        identificador=str(random.randint(0,2000))+correo
   
        if nombre and correo and edad and telefono and tipo_puesto and password:
            key = generate_password_hash(password, method = 'sha256')
            puestos=DB['puestos']
            puesto=Puesto(identificador,nombre,correo,edad,telefono,tipo_puesto,key,activo) 
            puestos.insert_one(puesto.datoPuestoJson())
            return redirect('/REGISTRAR-PUESTO')  
    
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO') 

def Operaciones_Puesto():  
    if 'usuario-administrador' in session:
        titulo="Operaciones puesto"
        puestos= DB ['puestos']
        puestosRecibidos=puestos.find()
        return render_template('ADMINISTRADOR/puestos/operaciones.html',titulo=titulo,puesto=puestosRecibidos)

    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

def Informacion_Puesto(key):
        titulo="Informacion puesto"
        puestos = DB['puestos']
        puestoOperativo = DB['operativos']
        operativo = puestoOperativo.find()    
        puestoRecibido=puestos.find_one({'identificador':key})
        return render_template('ADMINISTRADOR/puestos/informacion.html',titulo=titulo, puestos=puestoRecibido,operativo=operativo) 

def Eliminar_Puesto(key):
    puestos= DB['puestos']
    puestos.delete_one({'identificador':key})
    return redirect('/OPERACIONES-PUESTO')

def Actualizar_puesto(key,campo):
    puestos= DB['puestos']
    dato=request.form['dato']
    if dato:
        puestos.update_one({'identificador':key},{'$set':{campo:dato}})
    return Informacion_Puesto(key)      