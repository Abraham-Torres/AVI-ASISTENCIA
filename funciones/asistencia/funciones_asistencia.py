from flask import render_template, session, request, redirect
import time
from data_base import database as mongodb
from forms.ASISTENCIA.asistencia import Asistencia

DB = mongodb.dbConecction()


def AsistenciaDB():
    if 'usuario-administrador' in session:
        titulo = "Asistencia"
        asistenciaDB = DB['asistencia']
        asistencia = asistenciaDB.find()
        return render_template('/ADMINISTRADOR/asistencia/base_datos.html', titulo=titulo, asistencia=asistencia)
    elif 'usuario-empleado' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')


def AsistenciaApp():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')

    elif 'usuario-empleado' in session:
        datosPuestoDB = DB['puestos']
        asistenciaDB = DB['asistencia']
        DatosPuesto = datosPuestoDB.find_one(
            {'correo': session['usuario-empleado']})
        id = DatosPuesto['identificador']
        datosPuestoDB.update_one({'identificador': id}, {
                                 '$set': {'activo': True}})
        nombre = DatosPuesto['nombre']
        edad = DatosPuesto['edad']
        telefono = DatosPuesto['telefono']
        auxiliar = DatosPuesto['auxiliar']
        placas = request.form['placas']
        estado = request.form['EstadoOperativo']
        fecha = time.strftime('%d-%m-%y')
        identificador = str(fecha)+str(session['usuario-empleado'])
        inicio = time.strftime('%X')
        fin = '00:00:00'

        if identificador and nombre and edad and telefono and auxiliar and placas and estado and fecha and inicio and fin:
            asistencia = Asistencia(
                identificador, nombre, edad, telefono, auxiliar, placas, estado, fecha, inicio, fin)
            asistenciaDB.insert_one(asistencia.datosAsistenciaJson())
    return redirect('/HOME-APP')


def AsistenciaFinalizada():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
        datosPuestoDB = DB['puestos']
        asistenciaDB = DB['asistencia']
        DatosPuesto = datosPuestoDB.find_one(
            {'correo': session['usuario-empleado']})
        id = DatosPuesto['identificador']
        datosPuestoDB.update_one({'identificador': id}, {
                                 '$set': {'activo': False}})
        fecha = time.strftime('%d-%m-%y')
        hora = time.strftime('%X')
        identificador = str(fecha)+str(session['usuario-empleado'])
        asistenciaDB = DB['asistencia']
        asistenciaDB.update_one({'identificador': identificador}, {
                                '$set': {'fin': hora}})

        return redirect('/HOME-APP')
