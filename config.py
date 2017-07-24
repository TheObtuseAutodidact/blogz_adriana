
import os

# default config

DEBUG = False
SECRET_KEY = os.urandom(25)
# SQLALCHEMY_DATABASE_URI='mysql+pymysql://blogz:blogz@localhost:3306/blogz'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
