from pymongo import MongoClient #importamos mongo para la base de datos
import certifi #importamos certifi para que sea segura la conexion de base de datos

MONGO_URL = 'mongodb+srv://eduardo_sa:Cop07234EDU@system-ptmx.z3a6sag.mongodb.net/?retryWrites=true&w=majority'

ca=certifi.where()
def dbConecction():
    try:
        client = MongoClient(MONGO_URL,tlsCAfile=ca)
        db=client['AVI-ADMIN']
    except ConnectionError:
        print("Error en la bd")
    return db        
