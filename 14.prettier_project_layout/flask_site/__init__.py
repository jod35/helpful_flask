from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import DevConfig
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)
login_manager=LoginManager()
migrate=Migrate(app,db)
login_manager.init_app(app)

from . import views