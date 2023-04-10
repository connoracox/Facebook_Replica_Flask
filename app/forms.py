from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    confirm_password = PasswordField('confirm password', validators = [DataRequired(), EqualTo('password', message="Passwords must match!")])
    submit = SubmitField('Register')

class SignInForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    body = TextAreaField('Body', validators = [DataRequired()])
    submit = SubmitField('Submit Post')