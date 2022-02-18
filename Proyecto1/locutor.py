from conexiondb import obtener_conexion

def insertar_locutor(nombre,apellido,email):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Locutor(nombre,apellido,email) VALUES (%s, %s, %s)",
                       (nombre,apellido,email))
    conexion.commit()
    conexion.close()


def obtener_locutor():
    conexion = obtener_conexion()
    locutor = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_admon,nombre,apellido,email) FROM Locutor")
        locutor = cursor.fetchall()
    conexion.close()
    return locutor


def eliminar_locutor(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM Locutor WHERE id = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_locutor_por_id(id):
    conexion = obtener_conexion()
    locutor = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_admon,nombre,apellido,email FROM Locutor WHERE id = %s", (id))
        locutor = cursor.fetchone()
    conexion.close()
    return locutor


def actualizar_locutor(nombre,apellido,email, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE Locutor SET nombre = %s, apellido = %s, email = %s  WHERE id = %s",
                       (nombre,apellido,email, id))
    conexion.commit()
    conexion.close()

def obtener_locutor_por_email(email):
    conexion = obtener_conexion()
    locutor = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_locutor FROM Locutor WHERE email=%s", (email))
        locutor = cursor.fetchall()
    conexion.close()
    return locutor