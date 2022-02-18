from conexiondb import obtener_conexion

def insertar_concurso(nombre,id_admon,logo,url,fecha_inicio,fecha_fin,valor,guion,recomendacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Concurso(nombre,id_admon,logo,url,fecha_inicio,fecha_fin,valor,guion,recomendacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre,id_admon,logo,url,fecha_inicio,fecha_fin,valor,guion,recomendacion))
    conexion.commit()
    conexion.close()


def obtener_concurso():
    conexion = obtener_conexion()
    concurso = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_concurso,nombre,id_admon,logo,url,fecha_inicio,fecha_fin,valor,guion,recomendacion FROM Concurso order by fecha_inicio desc")
        concurso = cursor.fetchall()
    conexion.close()
    return concurso

def obtener_maxid():
    conexion = obtener_conexion()
    concurso = []
    with conexion.cursor() as cursor:
        cursor.execute("select id_concurso+1 from Concurso order by id_concurso desc limit 1")
        concurso = cursor.fetchall()
    conexion.close()
    return concurso

def eliminar_concurso(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM Concurso WHERE id_concurso = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_concurso_por_id(id):
    conexion = obtener_conexion()
    concurso = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_concurso,nombre,id_admon,logo,url,fecha_inicio,fecha_fin,valor,guion,recomendacion FROM Concurso WHERE id_concurso = %s", (id) )
        concurso = cursor.fetchone()
    conexion.close()
    return concurso


def actualizar_concurso(id,nombre,logo,fecha_inicio,fecha_fin,valor,guion,recomendacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE Concurso SET nombre = %s, logo = %s, fecha_inicio = %s, fecha_fin = %s, valor = %s, guion = %s, recomendacion = %s  WHERE id_concurso = %s",
                       (nombre,logo,fecha_inicio,fecha_fin,valor,guion,recomendacion,id))
    conexion.commit()
    conexion.close()