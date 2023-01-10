from flask import render_template, session, request, redirect
from data_base import database as mongodb
from werkzeug.security import generate_password_hash
from forms.ADMINISTRADOR.administrador import Administrador
import random


DB = mongodb.dbConecction()

def HomeSuper():
    if 'usuario-administrador' in session:
        titulo = 'SUPER SU'
        administradores = DB['administrador']
        adminTot = administradores.count_documents({})
        return render_template('/SUPERADMIN/super_su/index.html', titulo=titulo, Admin=adminTot)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

def FormularioNuevoAdmin():
    if 'usuario-administrador' in session:    
        titulo = "Agregar nuevo administrador"
        return render_template('/SUPERADMIN/super_su/registrar.html', titulo=titulo)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

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
            return redirect('/BASE-DATOS-ADMINISTRADORES')  
    
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO') 

def AdminDb():
    if 'usuario-administrador' in session:    
        titulo = "Base de datos administradores"
        AdministradorDB = DB['administrador']
        Admins = AdministradorDB.find()
        return render_template('/SUPERADMIN/super_su/base_datos.html',titulo=titulo,Admin=Admins)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

def Eliminar_Administrador(key):
    if 'usuario-administrador' in session:    
        AdministradorDB = DB['administrador']
        AdministradorDB.delete_one({'identificador':key})
        return redirect('/BASE-DATOS-ADMINISTRADORES')
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

def Informacion_Admin(key):
    if 'usuario-administrador' in session:        
        titulo="Informacion administrador"   
        AdministradorDB =DB['administrador']
        Administrador=AdministradorDB.find_one({'identificador':key})
        return render_template('SUPERADMIN/super_su/informacion.html',titulo=titulo, Admin=Administrador) 
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')    

def Actualizar_admin(key,campo):
    if 'usuario-administrador' in session:
        AdministradorDB = DB['administrador']
        dato = request.form['dato']
        if dato:
            AdministradorDB.update_one({'identificador':key},{'$set':{campo:dato}})  
        return AdminDb()            
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')    