from conexiondb import obtener_conexion

def insertar_admon(nombre,apellido,email,password):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Administrador(nombre,apellido,email,password) VALUES (%s, %s, %s, %s)",
                       (nombre,apellido,email,password))
    conexion.commit()
    conexion.close()


def obtener_admon():
    conexion = obtener_conexion()
    admon = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_admon,nombre,apellido,email,password) FROM Administrador")
        admon = cursor.fetchall()
    conexion.close()
    return admon


def eliminar_admon(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM Administrador WHERE id = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_admon_por_id(id):
    conexion = obtener_conexion()
    admon = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_admon,nombre,apellido,email,password FROM Administrador WHERE id = %s", (id))
        admon = cursor.fetchone()
    conexion.close()
    return admon

def obtener_admon_por_email(email):
    conexion = obtener_conexion()
    admon = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_admon,nombre,apellido,email,password FROM Administrador WHERE email = %s", (email))
        admon = cursor.fetchone()
    conexion.close()
    return admon


def actualizar_admon(nombre,apellido,email,password, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE Administrador SET nombre = %s, apellido = %s, email = %s, password = %s  WHERE id = %s",
                       (nombre,apellido,email,password))
    conexion.commit()
    conexion.close()