import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='test_site/.env')
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER=os.getenv('MAIL_SERVER')
    MAIL_PORT=os.getenv('MAIL_PORT')
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAIL_USE_SSL=True
    
    