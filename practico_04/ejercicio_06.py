"""Base de Datos SQL - Creación de tablas auxiliares"""
import sqlite3

from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    script = ("""CREATE TABLE IF NOT EXISTS PersonaPeso(id INTEGER PRIMARY KEY, fecha TEXT(10),
              peso TEXT(30), idPersona,FOREIGN KEY (idPersona) REFERENCES Persona (idPersona))""")

    cursor.execute(script)
    conn.commit()
    cursor.close()
    conn.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    script = "DROP TABLE IF EXISTS PersonaPeso"

    cursor.execute(script)
    conn.commit()
    cursor.close()
    conn.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
