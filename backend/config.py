import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
from decouple import config
# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
class Config:
    SECRET_KEY = config('SECRET_KEY')

# Connect to the database
class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProdConfig(Config):
    DEBUG=config('DEBUG')

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_ECHO=False