#IMPORTAMOS TODAS LAS LIBRERIAS QUE NECESITAREMOS
from flask import Flask

'''
Primero impprtamos de la carpeta funciones, la carpeta servidor (que contiene el archivo funciones_Servidor.py)
y le damos un alias.
Dentro de funciones_Servidor importamos render_template (este solo se importara donde sera usado no aqui en el index)
definimos una funcion, que esta va a contener todo lo que muestre el html (render_template)
Despues definimos otra funcion donde recibira los parametros establecidos
y retornamos el alis del archivo, ademas de la funcion que hicimos dentro de funciones_Servidor
'''
import funciones.servidor.funciones_Servidor as fun_serv
import funciones.homePage.funciones_HomePage as fun_home
import funciones.puestos.funciones_puestos as fun_puest
import funciones.puestosOperativos.funciones_puestosOperativos as fun_op
import funciones.estadosOperativos.funciones_estadosOperativos as fun_status
import funciones.asistencia.funciones_asistencia as fun_asist
import funciones.login.funciones_login as fun_log
import funciones.aplicacion.funciones_aplicacion as fun_app
import funciones.infoPerfilAdmin.funciones_PerfilAdmin as fun_admin



app=Flask(__name__)

app.secret_key= b'\xd0\xf7!ug\xb8/\x89:\x83\t&\x8c\xfa\xa6^'

#FUNCION DE HOMEPAGE
@app.route('/HOME')
def HomePage():
    return fun_home.Home()

#**********************************************************************************************
#FUNCION DE INFORMACION PERFIL
@app.route('/INFORMACION-ADMIN')
def InformacionAdmin():
    return fun_admin.InfoPerfil()

#FUNCION ACTUALIZAR CONTRASEÑA PERFIL 
@app.route('/ACTUALIZAR-CONTRASEÑA/<key>,<campo>',methods=['POST'])
def ActualizarContraseña(key, campo):
    return fun_admin.ActualizarPassword(key, campo)

#FUNCION DE INGRESAR NUEVO ADMIN (RUTA SECRETA)
@app.route('/', methods=['POST'])
def NuevoAdministrador():
    return     

#FUNCION ACTUALIZAR PERFIL
@app.route('/ACTUALIZAR-ADMINISTRADOR/<key>,<campo>', methods=['POST'])
def ActualizarAdministrador(key, campo):
    return fun_admin.ActualizarAdministrador(key, campo)
#**********************************************************************************************
#FUNCION PUESTO(FORMULARIO)
@app.route('/REGISTRAR-PUESTO')
def FormularioPuesto():
    return fun_puest.Formulario()

#FUNCION AGREGAR PUESTO
@app.route('/NUEVO-PUESTO',methods=['POST'])
def NuevoPuesto():
    return fun_puest.Nuevo()    
    
#FUNCION DE BD PUESTOS
@app.route('/BASE-DATOS-PUESTO')
def BaseDatos():
    return fun_puest.PuestoDb()

#FUNCION DE OPERACIONES PUESTO
@app.route('/OPERACIONES-PUESTO')
def Operaciones():
    return fun_puest.Operaciones_Puesto()

#FUNCION DE INFORMACION PUESTO
@app.route('/INFORMACION-PUESTO<key>')
def Informacion(key):
    return fun_puest.Informacion_Puesto(key)    

#FUNCION DE INFORMACION/ELIMINAR
@app.route('/ELIMINAR-PUESTO<key>')
def Eliminar_Puesto(key):
    return fun_puest.Eliminar_Puesto(key)

#FUNCION DE INFORMACION/ACTUALIZAR
@app.route('/ACTUALIZAR-PUESTO/<key>,<campo>',methods=['POST'])
def Actualizar_Puesto(key,campo):
    return fun_puest.Actualizar_puesto(key,campo)

#**********************************************************************************************
# FUNCION  DE DB DE PUESTOS OPERATIVOS
@app.route('/BASE-DATOS-PUESTOS-OPERATIVOS')
def BaseDatosOperativos():
    return fun_op.PuestoOperativoDb()

#FUNCION DE AGREGAR PUESTOS OPERATIVOS
@app.route('/NUEVO-PUESTO-OPERATIVO',methods = ['POST'])
def NuevoOperativo():
    return fun_op.NuevoPuestoOperativo()  

#FUNCION DE ELIMINAR PUESTO OPERATIVOS 
@app.route('/ELIMINAR-PUESTO-OPERATIVOS<key>')
def EliminarOperativo(key):
    return fun_op.EliminarPuestoOperativo(key)

#**********************************************************************************************   

#FUNCION DE DB DE ESTADOS OPERATIVOS
@app.route('/BASE-DATOS-ESTADOS-OPERATIVOS')
def BaseDatosEstados():
    return fun_status.EstadosOperativos()

#FUNCION DE AGREGAR NUEVO ESTADO OPERATIVO
@app.route('/NUEVO-ESTADO-OPERATIVO', methods=['POST'])  
def NuevoEstadoOperativo():
    return fun_status.NuevoEstado()  

#FUNCION DE ELIMINAR ESTADOS OPERATIVOS
@app.route('/ELIMINAR-ESTADO-OPERATIVO<key>')   
def EliminarEstadoOperativo(key):
    return fun_status.EliminarEstado(key) 

#**********************************************************************************************
#FUNCION DE DB DE ASISTENCIAS REGISTRADAS
@app.route('/ASISTENCIAS')
def BaseDatosAsistencia():
    return fun_asist.AsistenciaDB()
#**********************************************************************************************
#FUNCION DE SESION-ADMINISTRADOR.
@app.route('/')
@app.route('/INICIAR-SESION-ADMIN')
def iniciarSesionAdmins():
    return fun_log.IniciarSesion()

#FUNCION DE COMPROBAR SESION-ADMINISTRADOR
@app.route('/AUTENTICACION-ADMINISTRADOR', methods = ['POST'] )
def autenticacionSesionAdmins():
    return fun_log.AutenticacionAdmins()

#FUNCION DE CERRAR SESION ADMINISTRADOR
@app.route('/CERRAR-SESION-ADMINISTRADOR')
def CerrarSesionAdmins():
    return fun_log.CerrarSesionAdmin()     

#**********************************************************************************************
#FUNCIONES PARA PROOTEGER LAS RUTAS
@app.before_request
def VerificarSesiones():
    return fun_log.verificacion()

#**********************************************************************************************
#FUNCION DE LOGIN DE LA APP
@app.route('/INICIAR-SESION-EMPLEADO')
def IniciarSesionEmpleado():
    return fun_app.iniciarSesionApp()

#FUNCION DE CERRAR SESION DE APP
@app.route('/CERRAR-SESION-EMPLEADO')
def cerrarSesionEmpleado():
    return fun_app.CerrarSesionEmpleado()

#FUNCION DE COMPROBAR SESION-EMPLEADO
@app.route('/AUTENTICACION-APP', methods = ['POST'])
def autenticacionSesionEmpleado():
    return fun_app.AutenticacionEmpleado()

#FUNCION DE HOME PAGE DE LA APP
@app.route('/HOME-APP')
def HomeApp():
    return fun_app.homeAppPage()

#FUNCION DE REGISTRAR ASISTENCIA APP
@app.route('/ASISTENCIA-EMPLEADO', methods = ['POST'])
def AsistenciaEmpleado():
    return fun_asist.AsistenciaApp()    

@app.route('/ASISTENCIA-FINALIZADA')
def asistenciaEmpleadoFin():
    return fun_asist.AsistenciaFinalizada()

#**********************************************************************************************

#FUNCION DE PAGINA NO ENCONTRADA    
def Pagina_no_encontrada(error):
        return fun_serv.Error_404(error)

#**********************************************************************************************


#HACEMOS EL CONSTRUCTOR.
if __name__=='__main__':
    app.register_error_handler(404, Pagina_no_encontrada)
    app.run(host="0.0.0.0",debug=True)
    #CONFIGURAMOS EL HOST PARA QUE PUEDA ACCEDER DE CUALQUIER IP
    #Y TAMBIEN EL MODO DEBUG PARA VER LOS CAMBIOS EN TIEMPO REAL.