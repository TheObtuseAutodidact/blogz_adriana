from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config.from_pyfile('config.cfg')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from views import *



if __name__ == "__main__":
    app.run()
