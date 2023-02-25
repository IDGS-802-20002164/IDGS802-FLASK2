from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,SearchField, EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UseForm(Form):

    matricula = StringField('matricula',[
        validators.DataRequired(message='La matricula es requerida')]
                            )
    nombre = StringField('nombre',[
        validators.DataRequired(message='El campo es requerida'),
        validators.length(min=5,max=15,message='Ingresa un valor maximo')]
                        )
    apaterno = StringField('Apaterno',[mi_validacion])
    amaterno = StringField('Amaterno')
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario',[
        validators.DataRequired(message='El usuario es requerida')]
                            )
    password = PasswordField('contraeña',[
        validators.DataRequired(message='El campo es requerida'),
        validators.length(min=5,max=15,message='Ingresa un valor maximo')]
                        )
