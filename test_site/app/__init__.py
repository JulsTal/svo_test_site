from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager
import os
app=Flask(__name__, template_folder='templates')
app.debug=True
# app.config['SECRET_KEY']='7e\x97\x9a\xd3n\x7f35A\xb3\xda\rx\xa0\x18?S\x07\xc4^\x19\xef'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db_svo_sequrity.sqlite3'
app.config.from_object('config.Config')
db_svo_sequrity = SQLAlchemy(app)
mail=Mail(app)
from . import models, views, forms

db_svo_sequrity.create_all()
