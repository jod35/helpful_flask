from flask import render_template,request,redirect,flash #this method is used to render templates
from . import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,current_user
from .models import User,Post
from .forms import SignUpForm,LoginForm,PostForm    


@app.route('/')
def index():
   posts=Post.query.all()
   post_form=PostForm()
   args={
      'post_form':post_form,
   }
   return render_template('index.html',**args)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
   form=LoginForm()
   post_form=PostForm()
   username=request.form.get('username')
   password=request.form.get('password')
   user_exists=User.query.filter_by(username=username).first()

   args={
      'form':form
   }

   if user_exists and check_password_hash(user_exists.password_hash,password):
      login_user(user_exists)
      return redirect('/')

  
   return render_template('login.html',**args)

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