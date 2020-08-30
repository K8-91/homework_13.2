from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    #id = StringField('id', validators=[DataRequired()])
    artist = StringField('artist', validators=[DataRequired()])
    year_of_publication = StringField('year_of_publication', validators=[DataRequired()])
    CD_name = StringField('CD_name', validators=[DataRequired()])
    my_favourite = SelectField('my_favourite', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])





