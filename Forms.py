from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')