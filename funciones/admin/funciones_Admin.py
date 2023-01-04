from flask import render_template, session, request, redirect
from data_base import database as mongodb
from werkzeug.security import generate_password_hash
from forms.ADMINISTRADOR.administrador import Administrador
import random

DB = mongodb.dbConecction()


def InfoPerfil():
    if 'usuario-administrador' in session:
        titulo = 'Informacion administrador'
        AdministradorDB = DB['administrador']
        Administrador = AdministradorDB.find_one(
            {'correo': session['usuario-administrador']})
        return render_template('/ADMINISTRADOR/info_perfil/informacion_admin.html', titulo=titulo, administrador=Administrador)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')


def ActualizarPassword(key, campo):
    if 'usuario-administrador' in session:
        AdministradorDB = DB['administrador']
        dato = request.form['dato']
        if dato:
            dato = generate_password_hash(dato, method='sha256')
            AdministradorDB.update_one(
                {'correo': key}, {'$set': {campo: dato}})
        return InfoPerfil()
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
