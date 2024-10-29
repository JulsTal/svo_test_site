from datetime import datetime
from flask_login import UserMixin
from flask import  url_for
import re
from . import db_svo_sequrity
import sqlite3
def get_title_post(alias):
    try:
            # Выполнение запроса
            result = News.query.filter(News.url.like(alias)).first()
            if result:
                base = url_for('static', filename='images')
                text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          "\\g<tag>" + base + "/\\g<url>>",
                          result.text)
                return result.news_name, text
            else:
                return False, False
    except Exception as e:
        print("Ошибка при получении статьи: " + str(e))
        return False, False
# def get_title_post(alias):
#     try:
#         conn = sqlite3.connect('db_svo_sequrity.sqlite3')
#         cursor = conn.cursor()
#         cursor.execute("SELECT news_name, text FROM news WHERE url LIKE ? LIMIT 1", (alias,))
#         res = cursor.fetchone()
#         if res:
#             base = url_for('static', filename='images')
#             text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
#                           "\\g<tag>" + base + "/\\g<url>>",
#                           res[1])
#             return (res[0], text)
#     except sqlite3.Error as e:
#         print("Ошибка при получении статьи: " + str(e))
#     return (False, False)


class CardRazdel(db_svo_sequrity.Model):
    id=db_svo_sequrity.Column(db_svo_sequrity.Integer, primary_key=True)
    name_card=db_svo_sequrity.Column(db_svo_sequrity.Text, nullable=False)
    image=db_svo_sequrity.Column(db_svo_sequrity.String(255), nullable=False)
    address=db_svo_sequrity.Column(db_svo_sequrity.String(255), nullable=False)
    content=db_svo_sequrity.Column(db_svo_sequrity.String(255), nullable=False)
class News(db_svo_sequrity.Model):
      __tablename__="news"
      id=db_svo_sequrity.Column(db_svo_sequrity.Integer, primary_key=True)
      news_name=db_svo_sequrity.Column(db_svo_sequrity.Text, nullable=False)
      text=db_svo_sequrity.Column(db_svo_sequrity.Text, nullable=False)
      url=db_svo_sequrity.Column(db_svo_sequrity.Text, nullable=False)
      created_date=db_svo_sequrity.Column(db_svo_sequrity.DateTime, default=datetime.utcnow)
class User(db_svo_sequrity.Model, UserMixin):
       __tablename__='user'
       id=db_svo_sequrity.Column(db_svo_sequrity.Integer, primary_key=True)
       fio=db_svo_sequrity.Column(db_svo_sequrity.String(200), nullable=False)
       username=db_svo_sequrity.Column(db_svo_sequrity.String(20), nullable=False, unique=True)
       password=db_svo_sequrity.Column(db_svo_sequrity.String(15), nullable=False)

   