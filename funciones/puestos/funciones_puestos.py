from flask import render_template, request, redirect, session,flash
from data_base import database as mongodb
from forms.PUESTO.puesto import Puesto
import random
import pandas as pd
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
        titulo="Nuevo operador"
        AuxiliaresDB=DB['auxiliar']
        AuxiliaresRecibidos=AuxiliaresDB.find()
        return render_template('ADMINISTRADOR/puestos/registrar.html', titulo=titulo,auxiliar=AuxiliaresRecibidos)
       
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
            return redirect('/BASE-DATOS-OPERADOR')  
    
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
        auxiliares = DB['auxiliar']
        auxiliar = auxiliares.find()    
        puestoRecibido=puestos.find_one({'identificador':key})
        return render_template('ADMINISTRADOR/puestos/informacion.html',titulo=titulo, puestos=puestoRecibido,aux=auxiliar) 

def Eliminar_Puesto(key):
    puestos= DB['puestos']
    puestos.delete_one({'identificador':key})
    return redirect('/OPERACIONES-OPERADOR')

def Actualizar_puesto(key,campo):
    puestos= DB['puestos']
    dato=request.form['dato']
    if dato:
        puestos.update_one({'identificador':key},{'$set':{campo:dato}})
    return Informacion_Puesto(key)
    
def upload_operadores():
    file = request.files["upload_operadores"]
    operadores = DB['puestos']
   
    datos = []
    try: 
        excel = pd.read_excel(file,sheet_name='Sheet1',skiprows=1)
        for  index, row in excel.iterrows(): 
            def datoss():
                    return{
                    'identificador': str(row[0]),
                    'nombre': row[1],
                    'correo':row[2],
                    'edad': row[3],
                    'telefono': row[4],
                    'auxiliar':row[5],
                    'password':row[6],
                    'activo':bool(row[7])
                    }
            datos.append(datoss())
            print(datos)  
    except:
        flash('¡ERROR CON EL ARCHIVO EXCEL! POR FAVOR UTILIZAR LA PLATILLA') 
        return redirect('/BASE-DATOS-OPERADOR')
                
    try :
        operadores.insert_many(datos)
        return redirect('/BASE-DATOS-OPERADOR')
    except:
        print('ERROR CON LA INSERCION MONGO')
        return redirect('/BASE-DATOS-OPERADOR')