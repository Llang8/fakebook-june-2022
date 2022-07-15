from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    first_name = StringField('FirstName', validators = [DataRequired()])
    last_name = StringField('LastName', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('ConfirmPassword', validators = [DataRequired()])
    submit_button = SubmitField('Create my account')