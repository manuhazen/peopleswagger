import os
import connexion
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

basedir = os.path.abspath(os.path.dirname(__file__))

connection_app = connexion.App(__name__, specification_dir=basedir)

app = connection_app.app

# Configuring the database
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')

# Creating the SQLAlchemy Instance
db = SQLAlchemy(app)

# Creating the Marshmallow Instance
ma = Marshmallow(app)