from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,SearchField, EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class traductorForm(Form):

    español = StringField('español',[
        validators.DataRequired(message='La palabra es requerida')]
                            )
    ingles = StringField('ingles',[
        validators.DataRequired(message='La palabra es requerida')]
        )
class traductorForm2(Form):
    buscar = StringField('buscar'
                         )
