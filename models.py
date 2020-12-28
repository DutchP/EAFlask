
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(40),unique=True,nullable=False)
    body = db.Column(db.Text)

    def __init__(self,subject='',body=''):
        self.subject = subject
        self.body = body

    def __str__(self):
        return self.subject

class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False,unique=True)
    image_url = db.Column(db.String(220),nullable=False, unique=True)
    date_created= db.Column(db.DateTime(),nullable=False)
    description = db.Column(db.Text) 

    def __str__(self):
        return f"{self.name}, {self.image_url}"