"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    script = """DELETE FROM Persona WHERE idPersona = ?"""

    cursor.execute(script, (id_persona,))
    rs = cursor.rowcount

    conn.commit()
    cursor.close()
    conn.close()

    if rs >= 1:
        return True
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
