
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(40),unique=True,nullable=False)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime)

    def __init__(self,subject='',body=''):
        self.subject = subject
        self.body = body
        self.date_created = datetime.now()

    def __str__(self):
        return self.subject

class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False,unique=True)
    category = db.Column(db.String(),nullable=False)
    image_url = db.Column(db.String(220),nullable=False, unique=True)
    date_created= db.Column(db.DateTime)
    description = db.Column(db.Text) 

    def __init__(self,name='',category='',image_url='',date_created='',description=''):
        self.name = name
        self.category = category
        self.image_url = image_url
        self.date_created = date_created
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.image_url}"