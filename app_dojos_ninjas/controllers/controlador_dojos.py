from flask import Flask, render_template, request, redirect, session
from app_dojos_ninjas import app 
from app_dojos_ninjas.models.modelo_dojos import Dojo

@app.route('/dojos', methods = ['GET'])
def obtener_dojos():
    lista_dojos = Dojo.obtener_todos()
    return render_template ('dojos.html', lista_dojos = lista_dojos)

@app.route('/nuevo/dojo', methods = ['POST'])
def crear_dojos():
    nuevo_dojo = {
        "nombre": request.form['nombre']
    }
    Dojo.crear_uno(nuevo_dojo)
    return redirect ('/dojos')

@app.route( '/dojo/<int:id>', methods = ['GET'] )
def obtener_dojo( id ):
    data = {
        "id" : id
    }
    informacion_dojo = Dojo.obtener_uno_con_ninjas( data )
    return render_template( 'dojo.html', informacion_dojo = informacion_dojo )