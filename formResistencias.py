from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,SearchField, EmailField, SelectField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class resistenciaForm(Form):

    linea1 = SelectField('Selecciona un color B1',[
        validators.DataRequired(message='La palabra es requerida')],choices=[
        ('Negro', 'Negro'),
        ('Café', 'Café'),
        ('Rojo', 'Rojo'),
        ('Anaranjado', 'Anaranjado'),
        ('Amarillo', 'Amarillo'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Morado', 'Morado'),
        ('Gris', 'Gris'),
        ('Blanco', 'Blanco')
    ]
                            )
    
    linea2 = SelectField('Selecciona un color B2',[
        validators.DataRequired(message='La palabra es requerida')],choices=[
        ('Negro', 'Negro'),
        ('Café', 'Café'),
        ('Rojo', 'Rojo'),
        ('Anaranjado', 'Anaranjado'),
        ('Amarillo', 'Amarillo'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Morado', 'Morado'),
        ('Gris', 'Gris'),
        ('Blanco', 'Blanco')
    ]
                            )
    
    linea3 = SelectField('Selecciona un color B3',[
        validators.DataRequired(message='La palabra es requerida')],choices=[
        ('Negro', 'Negro'),
        ('Café', 'Café'),
        ('Rojo', 'Rojo'),
        ('Anaranjado', 'Anaranjado'),
        ('Amarillo', 'Amarillo'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Morado', 'Morado'),
        ('Gris', 'Gris'),
        ('Blanco', 'Blanco')
    ]
                            )

