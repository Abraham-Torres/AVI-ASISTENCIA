from flask import render_template, session, flash, request, redirect
from data_base import database as mongodb
from werkzeug.security import generate_password_hash, check_password_hash

DB = mongodb.dbConecction()

def IniciarSesion():
    titulo="iniciar sesion"
    return render_template('/ADMINISTRADOR/login/login.html',titulo=titulo)

def CerrarSesionAdmin():
    session.pop('usuario-administrador',None)
    return redirect('/INICIAR-SESION-ADMIN')

def AutenticacionAdmins():
    correo = request.form['correo']
    password = request.form['password']
    usuario = False
    if correo and password:
        Administrador = DB['administrador']
        AdminRecibido = Administrador.find_one({'correo':correo})
        if AdminRecibido:
            if(check_password_hash(AdminRecibido['password'], password)==True):
                session['usuario-administrador'] = AdminRecibido['correo']
                usuario = True
                session.pop('usuario-empleado',None)
                return redirect('/HOME')    
            elif(check_password_hash(AdminRecibido['password'],password)==False):
                flash('Error: Contraseña incorrecta')
        elif usuario == False:
            flash('Error: El usuario no existe')   
        return IniciarSesion()
    flash('Por favor llene todos los campos')      
    return IniciarSesion()

def verificacion():
    ruta = request.path
    if 'usuario-empleado' in session:
        pass
    elif not 'usuario-administrador' in session and ruta !="/INICIAR-SESION-ADMIN" and ruta !='/AUTENTICACION-ADMINISTRADOR' and ruta != "/AUTENTICACION-APP" and ruta !='/INICIAR-SESION-EMPLEADO' and not ruta.startswith("/static"):
        flash("inicia sesion para continuar")
        return redirect('/INICIAR-SESION-ADMIN')
    if 'usuario-administrador' in session:
        pass
    elif not 'usuario-empleado' in session and ruta !="/INICIAR-SESION-ADMIN" and ruta !='/AUTENTICACION-ADMINISTRADOR' and ruta != "/AUTENTICACION-APP" and ruta !='/INICIAR-SESION-EMPLEADO' and not ruta.startswith("/static"):
        flash("inicia sesion para continuar")
        return redirect('/INICIAR-SESION-EMPLEADO')

