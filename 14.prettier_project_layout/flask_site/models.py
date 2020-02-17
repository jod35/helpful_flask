from . import db,login_manager
from flask_login import UserMixin

class User(db.Model,UserMixin):
   id=db.Column(db.Integer,primary_key=True)
   username=db.Column(db.String(225),nullable=False)
   email=db.Column(db.String(225),nullable=False)
   password_hash=db.Column(db.Text(),nullable=False)

   def __str__(self):
      return self.username

class Post(db.Model):
   id=db.Column(db.Integer(),primary_key=True)
   title=db.Column(db.String(255),nullable=False)
   content=db.Column(db.Text(),nullable=False)

   def __str__(self):
      return self.title

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))