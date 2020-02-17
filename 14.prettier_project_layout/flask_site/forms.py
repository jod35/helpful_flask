from flask_wtf import FlaskForm #flask extension for Wtforms
from wtforms import StringField,PasswordField,SubmitField,TextAreaField #the needed fields
from wtforms.validators import DataRequired,Email,EqualTo
#to create forms
class LoginForm(FlaskForm):
   username=StringField("Username",validators=[DataRequired(message="The field is required.")])
   password=PasswordField("Password",validators=[DataRequired()])
   submit=SubmitField("Login")


class SignUpForm(FlaskForm):
   username=StringField("Username",validators=[DataRequired(message="The field is required.")])
   email=StringField("Email",validators=[DataRequired(message="The field is required."),Email("Please Enter a valid Email")])
   password=PasswordField("Password",validators=[DataRequired()])
   submit=SubmitField("Sign Up")


class PostForm(FlaskForm):
   title=StringField("Title",validators=[DataRequired()])
   content=TextAreaField("Content",validators=[DataRequired()])
   submit=SubmitField("Post")
