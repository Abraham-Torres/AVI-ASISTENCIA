# IMPORTAMOS TODAS LAS LIBRERIAS QUE NECESITAREMOS
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
import funciones.estadosOperativos.funciones_estadosOperativos as fun_status
import funciones.asistencia.funciones_asistencia as fun_asist
import funciones.login.funciones_login as fun_log
import funciones.aplicacion.funciones_aplicacion as fun_app
import funciones.admin.funciones_Admin as fun_admin
import funciones.superAdmin.funciones_superAdmin as fun_Super
import funciones.auxiliares.funciones_auxliar as fun_aux
import os


app = Flask(__name__)

app.secret_key = b'\xd0\xf7!ug\xb8/\x89:\x83\t&\x8c\xfa\xa6^'
app.host = "0.0.0.0"
app.port = os.getenv("PORT")
# ********************************FUNCIONES PARA EL HOME**************************************************************
# FUNCION DE HOMEPAGE
@app.route('/HOME')
def HomePage():
    return fun_home.Home()

#FUNCION DE API PARA GRAFICAS DINAMICAS
@app.route('/API')
def apiChart():
    return fun_home.Charts()    

# ********************************FUNCIONES PARA EL ADMINISTRADOR*****************************************************
# FUNCION DE INFORMACION PERFIL (VISTA)
@app.route('/INFORMACION-ADMIN')
def InformacionAdmin():
    return fun_admin.InfoPerfil()


#FUNCION ACTUALIZAR PERFIL
@app.route('/ACTUALIZAR-ADMINISTRADOR/<key>,<campo>', methods=['POST'])
def ActualizarAdministrador(key, campo):
    return fun_admin.ActualizarAdministrador(key, campo)

# FUNCION ACTUALIZAR CONTRASE??A PERFIL
@app.route('/ACTUALIZAR-CONTRASE??A/<key>,<campo>', methods=['POST'])
def ActualizarContrase??a(key, campo):
    return fun_admin.ActualizarPassword(key, campo)


# ******************************FUNCIONES PARA SUPER SU :)***********************************************************
# FUNCION DE HOME PAGE PARA SUPER SU
@app.route('/HOME-SUPER-SU')
def HomePageSuper():
    return fun_Super.HomeSuper()

# FUNCION DE INGRESAR NUEVO ADMIN (FORMULARIO)
@app.route('/REGISTRAR-ADMINISTRADOR')
def FormularioAdministrador():
    return fun_Super.FormularioNuevoAdmin()

# FUNCION DE REGISTRO DE NUEVO ADMINISTRADOR
@app.route('/NUEVO-ADMINISTRADOR', methods=['POST'])
def NuevoAdministrador():
    return fun_Super.NuevoAdmin()

# FUNCION DE BASE DE DATOS ADMNISTRADOR
@app.route('/BASE-DATOS-ADMINISTRADORES')
def BaseDatosAdmin():
    return fun_Super.AdminDb()

# FUNCION DE ELIMINAR ADMINISTRADOR
@app.route('/ELIMINAR-ADMINISTRADOR<key>')
def Eliminar_Admin(key):
    return fun_Super.Eliminar_Administrador(key)

# FUNCION DE INFORMACION ADMINISTRADOR
@app.route('/INFORMACION-ADMINISTRADOR<key>')
def Informacion_administrador(key):
    return fun_Super.Informacion_Admin(key)

# FUNCION DE INFORMACION/ACTUALIZAR ADMINISTRADOR
@app.route('/ACTUALIZAR-ADMINISTRADOR/<key>,<campo>', methods=['POST'])
def Actualizar_Admin(key, campo):
    return fun_Super.Actualizar_admin(key, campo)


# ****************************FUNCIONES PARA OPERADOR***********************************************************
# FUNCION OPERADOR(FORMULARIO)
@app.route('/REGISTRAR-OPERADOR')
def FormularioPuesto():
    return fun_puest.Formulario()

# FUNCION AGREGAR OPERADOR
@app.route('/NUEVO-OPERADOR', methods=['POST'])
def NuevoPuesto():
    return fun_puest.Nuevo()

# FUNCION DE BD OPERADOR
@app.route('/BASE-DATOS-OPERADOR')
def BaseDatos():
    return fun_puest.PuestoDb()

# FUNCION DE OPERACIONES OPERADOR
@app.route('/OPERACIONES-OPERADOR')
def Operaciones():
    return fun_puest.Operaciones_Puesto()

# FUNCION DE INFORMACION OPERADOR
@app.route('/INFORMACION-OPERADOR<key>')
def Informacion(key):
    return fun_puest.Informacion_Puesto(key)

# FUNCION DE INFORMACION/ELIMINAR
@app.route('/ELIMINAR-OPERADOR<key>')
def Eliminar_Puesto(key):
    return fun_puest.Eliminar_Puesto(key)

# FUNCION DE INFORMACION/ACTUALIZAR
@app.route('/ACTUALIZAR-PUESTO/<key>,<campo>', methods=['POST'])
def Actualizar_Puesto(key, campo):
    return fun_puest.Actualizar_puesto(key, campo)

# FUNCION DE UPDLOAD OPERADORES
@app.route('/UPLOAD-PUESTO', methods=['POST'])
def upload_operadores():
    return fun_puest.upload_operadores()
# **********************************FUNCIONES PARA AUXILIAR****************************************************
# FUNCION AUXILIAR(FORMULARIO)
@app.route('/REGISTRAR-AUXILIAR')
def Formulario_Aux():
    return fun_aux.Formulario_Aux()

# FUNCION AGREGAR AUXILIAR
@app.route('/NUEVO-AUXILIAR', methods=['POST'])
def NuevoAuxiliar():
    return fun_aux.Nuevo_Aux()

# FUNCION DE BD AUXILIAR
@app.route('/BASE-DATOS-AUXILIAR')
def BaseDatosAuxiliar():
    return fun_aux.AuxiliarDb()

# FUNCION DE OPERACIONES AUXILIAR
@app.route('/OPERACIONES-AUXILIAR')
def Operaciones_Aux():
    return fun_aux.Operaciones_Auxiliar()

# FUNCION DE INFORMACION
@app.route('/INFORMACION-AUXILIAR<key>')
def Informacion_Auxiliar(key):
    return fun_aux.Informacion_Aux(key)

# FUNCION DE INFORMACION/ELIMINAR
@app.route('/ELIMINAR-AUXILIAR<key>')
def Eliminar_Auxiliar(key):
    return fun_aux.Eliminar_Aux(key)

# FUNCION DE INFORMACION/ACTUALIZAR
@app.route('/ACTUALIZAR-AUXILIAR/<key>,<campo>', methods=['POST'])
def Actualizar_Auxiliar(key, campo):
    return fun_aux.Actualizar_Aux(key, campo)

# FUNCION DE UPDLOAD AUXILIARES
@app.route('/UPLOAD-AUXILIARES', methods=['POST'])
def upload_auxiliares():
    return fun_aux.upload_auxiliares()

# ********************************FUNCIONES PARA ESTADOS OPERATIVOS**********************************************

# FUNCION DE DB DE ESTADOS OPERATIVOS
@app.route('/BASE-DATOS-ESTADOS-OPERATIVOS')
def BaseDatosEstados():
    return fun_status.EstadosOperativos()

# FUNCION DE AGREGAR NUEVO ESTADO OPERATIVO
@app.route('/NUEVO-ESTADO-OPERATIVO', methods=['POST'])
def NuevoEstadoOperativo():
    return fun_status.NuevoEstado()

# FUNCION DE ELIMINAR ESTADOS OPERATIVOS
@app.route('/ELIMINAR-ESTADO-OPERATIVO<key>')
def EliminarEstadoOperativo(key):
    return fun_status.EliminarEstado(key)

# ********************************FUNCIONES DE ASISTENCIAS REGISTRADAS**************************
# FUNCION DE DB DE ASISTENCIAS REGISTRADAS
@app.route('/ASISTENCIAS')
def BaseDatosAsistencia():
    return fun_asist.AsistenciaDB()

# ********************************FUNCIONES DE SESION-ADMIN*************************************
# FUNCION DE SESION-ADMINISTRADOR.
@app.route('/')
@app.route('/INICIAR-SESION-ADMIN')
def iniciarSesionAdmins():
    return fun_log.IniciarSesion()

# FUNCION DE COMPROBAR SESION-ADMINISTRADOR
@app.route('/AUTENTICACION-ADMINISTRADOR', methods=['POST'])
def autenticacionSesionAdmins():
    return fun_log.AutenticacionAdmins()

# FUNCION DE CERRAR SESION ADMINISTRADOR
@app.route('/CERRAR-SESION-ADMINISTRADOR')
def CerrarSesionAdmins():
    return fun_log.CerrarSesionAdmin()

# *******************************FUNCIONES DE PROTECCION DE RUTAS********************************
# FUNCIONES PARA PROOTEGER LAS RUTAS
@app.before_request
def VerificarSesiones():
    return fun_log.verificacion()

# ******************************FUNCIONES PARA LA APP********************************************
# FUNCION DE LOGIN DE LA APP
@app.route('/INICIAR-SESION-EMPLEADO')
def IniciarSesionEmpleado():
    return fun_app.iniciarSesionApp()

# FUNCION DE CERRAR SESION DE APP
@app.route('/CERRAR-SESION-EMPLEADO')
def cerrarSesionEmpleado():
    return fun_app.CerrarSesionEmpleado()

# FUNCION DE COMPROBAR SESION-EMPLEADO
@app.route('/AUTENTICACION-APP', methods=['POST'])
def autenticacionSesionEmpleado():
    return fun_app.AutenticacionEmpleado()

# FUNCION DE HOME PAGE DE LA APP
@app.route('/HOME-APP')
def HomeApp():
    return fun_app.homeAppPage()

# FUNCION DE INFORMACION DE PERFIL
@app.route('/INFORMACION-PERFIL-EMPLEADO')
def InformacionPerfilEmpleado():
    return fun_app.InformacionEmpleado()

# FUNCION DE ACTUALIZAR CONTRASE??A PERFIL
@app.route('/ACTUALIZAR-CONTRASE??A-EMPLEADO/<key>,<campo>', methods=['POST'])
def ActualizarContrase??aEmpleado(key, campo):
    return fun_app.ActualizarPasswordEmpleado(key, campo)

# FUNCION DE REGISTRAR ASISTENCIA APP
@app.route('/ASISTENCIA-EMPLEADO', methods=['POST'])
def AsistenciaEmpleado():
    return fun_asist.AsistenciaApp()


@app.route('/ASISTENCIA-FINALIZADA')
def asistenciaEmpleadoFin():
    return fun_asist.AsistenciaFinalizada()

# **********************************************************************************************

# FUNCION DE PAGINA NO ENCONTRADA
def Pagina_no_encontrada(error):
    return fun_serv.Error_404(error)

# **********************************************************************************************

# HACEMOS EL CONSTRUCTOR.
if __name__ == '__main__':
    app.register_error_handler(404, Pagina_no_encontrada)
    app.run(host=app.host, port=app.port, debug=True)
    # CONFIGURAMOS EL HOST PARA QUE PUEDA ACCEDER DE CUALQUIER IP
    # Y TAMBIEN EL MODO DEBUG PARA VER LOS CAMBIOS EN TIEMPO REAL.
