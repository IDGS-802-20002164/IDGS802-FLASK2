from flask import Flask, render_template
from flask import request
import formsTraductor


app = Flask(__name__)


@app.route("/traductor",methods=["GET","POST"])
def traductor():
    palabras= formsTraductor.traductorForm(request.form)
    palabras2= formsTraductor.traductorForm2(request.form)
    mat=''
    nom=''
    palabra = ''
    palabraslist = ""
    res = ''
    btn = request.form.get("btn")
    btn2 = request.form.get("a")

    if request.method == 'POST':

        if btn2 == 'Registrar' and palabras.validate():
                mat = palabras.español.data.upper()
                nom = palabras.ingles.data.upper()
                f = open('traductor.txt','a')
                f.write(nom + ":" + mat +'\n')
                f.close()
        
        if  btn == 'buscar':
            palabra = palabras2.buscar.data.upper()
            opc = request.form.get("drone")
            if opc == "1":
                f = open('traductor.txt','r')
                palabraslist = f.readlines()

                for valor in palabraslist:
                    arr = valor.replace("\n","").split(":")
                
                    if palabra == arr[1]:
                        res = arr[0]
                f.close()
            
            if opc == "2":
                f = open('traductor.txt','r')
                palabraslist = f.readlines()

                for valor in palabraslist:
                    arr = valor.replace("\n","").split(":")
                
                    if palabra == arr[0]:
                        res = arr[1]
                f.close()

        

    return render_template("traductor.html",form=palabras,form2=palabras2,pal=res)




if __name__ =="__main__":
    app.run(debug=True, port=3000)