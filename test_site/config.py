import os

class Config(object):
    SQLALCHEMY_DATABASE_URI='sqlite:///db_svo_sequrity.sqlite3'
    SECRET_KEY='apple pay'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME = 'juliatalaeva8881@gmail.com'
    MAIL_PASSWORD= 'voaf hswc szdh dseg'
    MAIL_USE_SSL=True
    
    