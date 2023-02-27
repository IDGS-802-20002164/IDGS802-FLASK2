from flask import Flask, render_template
from flask import request
import formResistencias
from flask import flash
from flask import make_response
from flask_wtf.csrf import CSRFProtect
from bs4 import BeautifulSoup
from jinja2 import Template


app = Flask(__name__)
app.config['SECRET_KEY'] = "Esta es una clave encriptada"
csrf= CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print('numero1')



@app.route("/resistencias",methods=["GET","POST"])
def resistencias():
    print('numero2')
    resis = formResistencias.resistenciaForm(request.form)
    color1 = ''
    color2 = ''
    color3 = ''
    color4 = ''
    num1 = ''
    num2 = ''
    num3 = 0
    num = ''
    valor = 0
    opc = ''
    maxi = 0
    mini = 0
    color = 'red'

    banda3 = 0
    if request.method == 'POST':
        
        opc = request.form.get("drone")

        if opc == "1":
            color1 = resis.linea1.data
            color2 = resis.linea2.data
            color3 = resis.linea3.data

            num1 = str(calcularres(color1))
            num2 = str(calcularres(color2))
            num = num1+num2
            banda3 = 10 **(calcularres(color3))
            valor = banda3 * int(num)
            color4 = 'Dorado'
            num3 = valor * .05
            maxi = valor + num3
            mini = valor - num3
            
        if opc == "2":
            color1 = resis.linea1.data
            color2 = resis.linea2.data
            color3 = resis.linea3.data

            num1 = str(calcularres(color1))
            num2 = str(calcularres(color2))
            num = num1+num2
            banda3 = 10 **(calcularres(color3))
            valor = banda3 * int(num)
            color4 = 'Plata' 
            num3 = valor * .10
            mini = valor - num3
            maxi = valor + num3

    
    datos = ''
    if request.method=='POST' :
        col = color1
        col2= color2
        col3 = color3
        col4= color4
        datos = col+' '+ col2 + ' ' + col3+' '+ col4
        succes_message = 'Tus colores son {}'.format(datos)
        flash(succes_message)

   
    response = make_response(render_template("resistencias.html",form = resis,color1 = color1,color2 = color2,color3 = color3,
                            valor=valor, color4 = color4, mini=mini,maxi=maxi))
    response.set_cookie('dato_user',datos)
    return response
            
@app.after_request
def after_request(response):
    print('numero3')
    return response
    


def calcularres(color):
    banda = 0 
    if color == 'Negro':
        banda = 0
    elif color == 'Café':
        banda = 1
    elif color == 'Rojo':
        banda = 2
    elif color == 'Anaranjado':
        banda = 3
    elif color == 'Amarillo':
        banda = 4
    elif color == 'Verde':
        banda = 5
    elif color == 'Azul':
        banda = 6
    elif color == 'Morado':
        banda = 7
    elif color == 'Gris':
        banda = 8
    elif color == 'Blanco':
        banda = 9
    return banda



if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)