from flask import render_template
from data_base import database as mongodb

DB = mongodb.dbConecction()

def Home():
    titulo="Inicio"
    return render_template('/index.html',titulo=titulo)

    