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

# Trae todas las noticias guardadas (las mas nuevas primero)
def obtener_noticias():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM noticias ORDER BY id DESC")
        noticias = cursor.fetchall()
    conexion.close()
    return noticias

@app.route('/')
def index():
    try:
        noticias = obtener_noticias()
        return render_template('index.html', noticias=noticias)
    except Exception as e:
        return render_template('index.html', noticias=[], mensaje=f"Hubo un error: {e}")

@app.route('/guardar', methods=['POST'])
def guardar():
    titulo = request.form['titulo']
    red_social = request.form['red_social']
    enlace = request.form['enlace']
    estado = request.form['estado']
    fecha = request.form['fecha']

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO noticias (titulo, red_social, enlace, estado, fecha) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (titulo, red_social, enlace, estado, fecha))
            conexion.commit()
        conexion.close()
        mensaje = "Noticia registrada"
        noticias = obtener_noticias()
    except Exception as e:
        mensaje = f"Hubo un error: {e}"
        noticias = []

    return render_template('index.html', mensaje=mensaje, noticias=noticias)

if __name__ == '__main__':
    app.run(debug=True)
