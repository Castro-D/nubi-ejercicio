import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'app.db')
CONTRASENIA = 'contrasenia_desarrollo'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
