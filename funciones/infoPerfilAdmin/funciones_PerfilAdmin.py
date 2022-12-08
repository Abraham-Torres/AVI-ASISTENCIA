from flask import render_template, session, request, redirect
from data_base import database as mongodb
from werkzeug.security import generate_password_hash
from forms.ADMINISTRADOR.administrador import Administrador
import random



DB = mongodb.dbConecction()

def InfoPerfil():
    titulo = 'Informacion administrador'
    AdministradorDB = DB['administrador']
    Administrador = AdministradorDB.find_one({'correo':session['usuario-administrador']})
    return render_template('/ADMINISTRADOR/info_perfil/informacion_admin.html',titulo = titulo, administrador = Administrador)

def FormularioAdmin():
    return

def NuevoAdmin():
    if 'usuario-administrador' in session:
        nombre=request.form['nombre']
        correo=request.form['correo']
        password=request.form['password']
        identificador=str(random.randint(0,2000))+correo
   
        if nombre and correo and password:
            key = generate_password_hash(password, method = 'sha256')
            AdministradorDB = DB['administrador']
            administrador = Administrador(identificador,nombre,correo,key) 
            AdministradorDB.insert_one(administrador.datosAdministradorJson())
            return redirect('/REGISTRAR-ADMINISTRADOR')  
    
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO') 

def ActualizarAdministrador(key, campo):
    AdministradorDB = DB['administrador']
    dato = request.form['dato']
    if dato:
        AdministradorDB.update_one({'identificador':key},{'$set':{campo:dato}})
        return InfoPerfil() 
    return           

def ActualizarPassword(key,campo):
    AdministradorDB = DB['administrador']
    dato=request.form['dato']
    if dato:
        dato = generate_password_hash(dato, method = 'sha256')
        AdministradorDB.update_one({'correo':key},{'$set':{campo:dato}})
        print(dato)
    return InfoPerfil()

