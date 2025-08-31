from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido', validators=[DataRequired()])
    membership = IntegerField('Membresia', validators=[DataRequired()])
    save_b = SubmitField('Save')