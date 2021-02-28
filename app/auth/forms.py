from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Enter your password',validators=[Required(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('That email address already exists')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    password = PasswordField('Enter your password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')