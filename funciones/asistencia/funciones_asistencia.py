from flask import render_template, session, request, redirect
import time
from data_base import database as mongodb
from forms.ASISTENCIA.asistencia import Asistencia

DB = mongodb.dbConecction()

def AsistenciaDB():
    titulo = "Asistencia"
    asistenciaDB = DB['asistencia']
    asistencia = asistenciaDB.find()
    return render_template('/ADMINISTRADOR/asistencia/base_datos.html',titulo=titulo,asistencia=asistencia)

def AsistenciaApp():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
         datosPuestoDB = DB['puestos']
         asistenciaDB = DB['asistencia']
         DatosPuesto = datosPuestoDB.find_one({'correo':session['usuario-empleado']})
         id = DatosPuesto['identificador']
         datosPuestoDB.update_one({'identificador':id},{'$set':{'activo':True}})
         nombre = DatosPuesto['nombre']
         fecha = time.strftime('%d-%m-%y')
         puesto = DatosPuesto['tipo_puesto']
         identificador = str(fecha)+str(session['usuario-empleado'])
         operativo = request.form['EstadoOperativo']
         inicio = time.strftime('%X')
         fin = '00:00:00'

         if identificador and nombre and fecha and inicio and operativo and puesto and fin:
            asistencia=Asistencia(identificador, nombre, fecha, inicio, operativo, puesto, fin)
            asistenciaDB.insert_one(asistencia.datosAsistenciaJson())
    return redirect('/HOME-APP')      

def AsistenciaFinalizada():
    datosPuestoDB = DB['puestos']
    DatosPuesto = datosPuestoDB.find_one({'correo':session['usuario-empleado']})
    id = DatosPuesto['identificador']
    datosPuestoDB.update_one({'identificador':id},{'$set':{'activo':False}})
    fecha = time.strftime('%d-%m-%y')
    hora = time.strftime('%X')
    identificador = str(fecha)+str(session['usuario-empleado'])
    asistenciaDB = DB['asistencia']
    asistenciaDB.update_one({'identificador':identificador},{'$set':{'fin':hora}})
    return redirect('/HOME-APP')



