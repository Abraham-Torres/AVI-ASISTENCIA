from flask import render_template, request, session, redirect, flash
from data_base import database as mongodb
from werkzeug.security import check_password_hash, generate_password_hash


DB = mongodb.dbConecction()


def iniciarSesionApp():
    titulo = 'Iniciar sesion empleado'
    return render_template('/APLICACION/login/login.html', titulo=titulo)


def CerrarSesionEmpleado():
    session.pop('usuario-empleado', None)
    return redirect('/INICIAR-SESION-EMPLEADO')


def AutenticacionEmpleado():
    correo = request.form['correo']
    password = request.form['password']
    usuario = False
    if correo and password:
        Empleado = DB['puestos']
        EmpleadoRecibido = Empleado.find_one({'correo': correo})
        if EmpleadoRecibido:
            if (check_password_hash(EmpleadoRecibido['password'], password) == True):
                session['usuario-empleado'] = EmpleadoRecibido['correo']
                usuario = True
                session.pop('usuario-administrador', None)
                return redirect('/HOME-APP')
            elif (check_password_hash(EmpleadoRecibido['password'], password) == False):
                flash('Error: La contraseña es incorrecta')
        elif usuario == False:
            flash('Error: Usuario incorrecto o no existe')
        return iniciarSesionApp()
    flash('No se han insertado datos en el formulario')
    return iniciarSesionApp()


def homeAppPage():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
        titulo = 'Incio APP'
        datosPuestoDB = DB['puestos']
        datosEstadoDB = DB['estadoscat']
        Estado = datosEstadoDB.find()
        puestos = datosPuestoDB.find_one(
            {'correo': session['usuario-empleado']})
        return render_template('/APLICACION/index.html', titulo=titulo, Estado=Estado, puestos=puestos)


def InformacionEmpleado():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
        titulo = 'Informacion empleado'
        EmpleadoDB = DB['puestos']
        Empleado = EmpleadoDB.find_one({'correo': session['usuario-empleado']})
        return render_template('/APLICACION/informacion_empleado.html', titulo=titulo, operador=Empleado)


def ActualizarPasswordEmpleado(key, campo):
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
        EmpleadoDB = DB['puestos']
        dato = request.form['dato']
        if dato:
            dato = generate_password_hash(dato, method='sha256')
            EmpleadoDB.update_one({'correo': key}, {'$set': {campo: dato}})
        return InformacionEmpleado()
