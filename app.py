from flask import Flask, render_template
from flask import request
from collections import Counter
import app_Numeros
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = "Esta es una clave encriptada"
csrf= CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@app.before_request
def before_request():
    print('numero1')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


@app.route("/cookies",methods = ['GET','POST'])
def cookies():
    print('numero2')
    reg_user = forms.LoginForm(request.form)
    datos = ''
    if request.method=='POST' and reg_user.validate():
        user = reg_user.username.data
        passw= reg_user.password.data
        datos = user+'@'+ passw
        succes_message = 'Bienvenido {}'.format(user)
        flash(succes_message)

    response = make_response(render_template('cookies.html',form=reg_user))
    response.set_cookie('dato_user',datos)
    return response

#********************************************************************************

@app.after_request
def after_request(response):
    print('numero3')
    return response


@app.route("/saludo")
def saludo():
    valor_cookie= request.cookies.get('dato_user')
    nombre = valor_cookie.split('@')
    return render_template('saludo.html',nom=nombre[0])

#**************************************************************************************

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():

    alum_form = forms.UseForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST' and alum_form.validate():
        mat = alum_form.matricula.data
        nom = alum_form.nombre.data
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data
    return render_template("Alumnos.html",form=alum_form, mat = mat, nom = nom)


@app.route("/CajasDi", methods=['GET','POST'])
def CajasDi():
    reg_caja= app_Numeros.CajaForm(request.form)
    if request.method=='POST':
        btn = request.form.get("btn")
        if btn == 'Cargar':
            return render_template('Numeros.html',form=reg_caja)
        if btn == 'Datos':
            numero = request.form.getlist("numeros")
            max_value = None
            for num in numero:
                if (max_value is None or num > max_value):
                    max_value = num

            min_value = None
            for num in numero:
                if (min_value is None or num < min_value):
                    min_value = num

            for i in range(len(numero)):
                numero[i] = int(numero[i])
            prom = 0
            prom = sum(numero) / len(numero)
            counter = Counter(numero)
            resultados = counter.most_common()
            textoResultado = ''
            for r in resultados:
                if r[1] > 1:
                    textoResultado += '<p>El número {0} se repite {1}</p>'.format(r[0], r[1])
            return render_template('Numeros.html',form=reg_caja, 
            max_value=max_value, min_value=min_value, prom=prom, repetidos = textoResultado)
    return render_template('Numeros.html', form=reg_caja)


if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)