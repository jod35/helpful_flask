from flask import Flask,render_template,request,redirect,flash #this method is used to render templates
from flask_wtf import FlaskForm #flask extension for Wtforms
from wtforms import StringField,PasswordField,SubmitField,TextAreaField #the needed fields
from wtforms.validators import DataRequired,Email,EqualTo
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user     

import os


app=Flask(__name__)
app.secret_key='6f909e25bf1eae9b01de1abc'

class Config:
   SQLALCHEMY_DATABASE_URI='mysql://jon:nathanoj35@localhost/my_data'
   SQLALCHEMY_TRACK_MODIFICATIONS=False

app.config.from_object(Config)
db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)



class User(db.Model,UserMixin):
   id=db.Column(db.Integer,primary_key=True)
   username=db.Column(db.String(225),nullable=False)
   email=db.Column(db.String(225),nullable=False)
   password_hash=db.Column(db.Text(),nullable=False)

   def __str__(self):
      return self.username

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


#fake in memory database containing post data


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

#to create database models



posts=[
   {
      'author':"Harry Porter",
      'date_posted':"Sat 15 Feb 2020",
      'title':"A day in Portland",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },
   {
      'author':"John Doe",
      'date_posted':"Sat 15 Feb 2020",
      'title':"How was Valentine?",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },
   {
      'author':"Jane Doe",
      'date_posted':"Sat 15 Feb 2020",
      'title':"One African survived coronavirus",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },

]

@app.route('/')
def index():

   return render_template('index.html',posts=posts)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
   form=LoginForm()
   username=request.form.get('username')
   password=request.form.get('password')
   user_exists=User.query.filter_by(username=username).first()

   if user_exists and check_password_hash(user_exists.password_hash,password):
      login_user(user_exists)
      return redirect('/')

   else:
      flash("Invalid login")
      return redirect('/login')
   return render_template('login.html',form=form)

@app.route('/signup',methods=['GET', 'POST'])
def create_account():
   form=SignUpForm()
   if request.method == 'POST':
      username=request.form.get('username')
      email=request.form.get('email')
      password=generate_password_hash(request.form.get('password'))

      new_user=User(
         username=username,
         email=email,
         password_hash=password
      )
      db.session.add(new_user)
      db.session.commit()
      flash("User Created successfully")
      return redirect('/')
   return render_template('signup.html',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)