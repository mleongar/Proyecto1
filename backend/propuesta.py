from conexiondb import obtener_conexion

def insertar_Propuesta(fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Propuesta(fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje))
    conexion.commit()
    conexion.close()


def obtener_Propuesta():
    conexion = obtener_conexion()
    Propuesta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_propuesta,fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje) FROM Propuesta")
        Propuesta = cursor.fetchall()
    conexion.close()
    return Propuesta


def eliminar_Propuesta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM Propuesta WHERE id_propuesta = %s", (id))
    conexion.commit()
    conexion.close()

def eliminar_Propuesta_concurso(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM Propuesta WHERE id_concurso = %s", (id))
    conexion.commit()
    conexion.close()

def obtener_Propuesta_por_id(id):
    conexion = obtener_conexion()
    Propuesta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_propuesta,fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje FROM Propuesta WHERE id = %s", (id))
        Propuesta = cursor.fetchone()
    conexion.close()
    return Propuesta


def actualizar_Propuesta(id,fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE Propuesta SET fecha = %s, id_locutor = %s, id_concurso = %s, estado = %s, voz_original = %s, voz_convertida = %s, mensaje = %s  WHERE id = %s",
                       (fecha,id_locutor,id_concurso,estado,voz_original,voz_convertida,mensaje))
    conexion.commit()
    conexion.close()

def obtener_Propuesta_por_concurso(id):   
    conexion = obtener_conexion()
    Propuesta = []
    with conexion.cursor() as cursor:
      cursor.execute("SELECT Propuesta.fecha, Propuesta.estado, Propuesta.voz_original, Propuesta.voz_convertida, Propuesta.mensaje, Locutor.nombre, Locutor.apellido, Locutor.email FROM Propuesta INNER JOIN Locutor ON Propuesta.id_locutor = Locutor.id_locutor WHERE Propuesta.id_concurso = %s order by Propuesta.fecha desc", (id))
      Propuesta = cursor.fetchall()
    conexion.close()
    return Propuesta

def obtener_Propuesta_por_concurso_por_locutor():   
    conexion = obtener_conexion()
    Propuesta = []
    with conexion.cursor() as cursor:
      cursor.execute("SELECT Propuesta.voz_convertida, Locutor.nombre, Concurso.nombre  FROM Propuesta INNER JOIN Locutor ON Propuesta.id_locutor = Locutor.id_locutor INNER JOIN Concurso ON Propuesta.id_concurso = Concurso.id_concurso")
      Propuesta = cursor.fetchall()
    conexion.close()
    return Propuesta