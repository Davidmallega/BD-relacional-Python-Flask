import mysql.connector

def crear_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rafaela13.",
        database="TuMejorOferta"
    )

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
    print("Conexión cerrada.")