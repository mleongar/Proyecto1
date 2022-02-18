import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='cloud',
                                password='uniandeS.1',
                                db='supervoices')
