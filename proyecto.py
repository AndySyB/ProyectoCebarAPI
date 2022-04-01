from sqlite3 import Cursor
from flask import Flask
from flask import render_template, request, redirect, url_for, flash, jsonify, make_response, session
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime, timedelta
from functools import wraps
import os
from jwt import api_jwt, api_jws

app = Flask(__name__)
app.config['SECRET_KEY'] = "APICEBAR54132F321HG564"
key = "APICEBAR54132F321HG564"
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'Localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Cebar'
mysql.init_app(app)

def token_required(func):
    
    @wraps(func)
    def decorated(*args,**kwargs):
       
        toke = request/args.get('token')
        if not token:
            return jsonify({'Alerta!':'El token es inexistente!'})
        try:
            payload = api_jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alerta!': 'Token invalido!'})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/')

def login():
    if not  session.get('logged_in'):
        return render_template('votantes/login.html')
    else:

        return redirect(url_for('index'))

@app.route('/authenticate', methods=['POST'])
def authenticate():
    
    _user=request.form['txtuser']
    _password=request.form['txtPassword']
    sql ="SELECT * FROM  user where Nombre=%s and Password= %s"
    datos=(_user, _password)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    votantes=cursor.fetchall()
    if votantes != 0:
        session['logged_in']=True
       
        token = api_jwt.encode({
        'user':request.form['txtuser'],
        'expiration': request.form['txtPassword']
         },
            key)
        return render_template('votantes/index.html')
    else:
        return render_template('votantes/login.html')



@app.route('/index')
def index(): 

    sql ="SELECT * FROM `dvotantes`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    
    dvotantes=cursor.fetchall()
    print(dvotantes)
    
    conn.commit()
    return render_template('votantes/index.html', dvotantes=dvotantes)


@app.route('/destroy/<int:id_votante>')
def destroy(id_votante):
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM dvotantes WHERE id_votante=%s",(id_votante))
    conn.commit()
    return redirect('votantes/index.html')


@app.route('/edit/<int:id_votante>')
def edit(id_votante):
    
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM dvotantes WHERe id_votante=%s", (id_votante))
     dvotantes=cursor.fetchall()
     conn.commit()
     
     return render_template('votantes/edit.html',dvotantes=dvotantes)
 

@app.route('/update', methods=['POST'])
def update():
    _nombres=request.form['txtNombre']
    _apellidos=request.form['txtApellidos']
    _direccion=request.form['txtDirección']
    _telefono=request.form['txtTeléfono']
    _cedula=request.form['txtCédula']
    _lider=request.form['txtLider']
    _barrio=request.form['txtBarrio']
    _puesto=request.form['txtPuesto']
    _mesa=request.form['txtMesa']
    
    id_votante=request.form['txtID']
    
    sql = "UPDATE `dvotantes` SET Nombres=%s, Apellidos=%s, Dirección=%s, Teléfono=%s, Cédula=%s, Lider_id=%s, Barrio_id=%s, Puestovotacion_id=%s, mesa=%s WHERE id_votante=%s;"
    
    datos=(_nombres,_apellidos,_direccion,_telefono,_cedula,_lider,_barrio,_puesto,_mesa,id_votante)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('votantes/index.html')
    


@app.route('/create')
def create():
    return render_template('votantes/create.html')



@app.route('/store', methods=['POST'])
def storage():
    
    _nombres=request.form['txtNombre']
    _apellidos=request.form['txtApellidos']
    _direccion=request.form['txtDirección']
    _telefono=request.form['txtTeléfono']
    _cedula=request.form['txtCédula']
    _lider=request.form['txtLider']
    _barrio=request.form['txtBarrio']
    _puesto=request.form['txtPuesto']
    _mesa=request.form['txtMesa']
    
    if _nombres=='' or _apellidos== '' or _direccion=='' or _telefono=='' or _cedula=='' or _lider=='' or _barrio=='' or _puesto=='' or _mesa=='':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('create'))
    
    
    sql = "INSERT INTO `dvotantes` (`Id_votante`, `Nombres`, `Apellidos`, `Dirección`, `Teléfono`, `Cédula`, `Lider_id`, `Barrio_id`, `Puestovotacion_id`, `mesa`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos=(_nombres,_apellidos,_direccion,_telefono,_cedula,_lider,_barrio,_puesto,_mesa)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')
          

if __name__ == '__main__':
    app.run(debug=True)
