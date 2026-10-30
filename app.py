from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Configuracion de conexion para la base de datos en phpMyAdmin
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='fakenews_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Trae todos los reportes guardados (los mas nuevos primero)
def obtener_reportes():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM reportes ORDER BY id DESC")
        reportes = cursor.fetchall()
    conexion.close()
    return reportes

@app.route('/')
def index():
    try:
        reportes = obtener_reportes()
        return render_template('index.html', reportes=reportes)
    except Exception as e:
        return render_template('index.html', reportes=[], mensaje=f"Hubo un error: {e}")

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha = request.form['fecha']
    red_social = request.form['red_social']
    reporte = request.form['reporte']

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO reportes (nombre, apellido, fecha, red_social, reporte) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apellido, fecha, red_social, reporte))
            conexion.commit()
        conexion.close()
        mensaje = "Reporte registrado"
        reportes = obtener_reportes()
    except Exception as e:
        mensaje = f"Hubo un error: {e}"
        reportes = []

    return render_template('index.html', mensaje=mensaje, reportes=reportes)

if __name__ == '__main__':
    app.run(debug=True, reloader_type='stat')