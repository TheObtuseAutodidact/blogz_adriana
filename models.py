from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app import db, bcrypt

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, server_default=None)
    author_id = db.Column(db.Integer, ForeignKey('user.id'))

    def __init__(self, title, body, pub_date, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.pub_date = pub_date

    def __repr__(self):
        return 'title: {} written by {}'.format(self.title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(560))
    posts = relationship("Post", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<name - {}>'.format(self.name)
