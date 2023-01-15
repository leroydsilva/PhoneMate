import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
from decouple import config
from dotenv import load_dotenv
# Enable debug mode.
DEBUG = True
load_dotenv()

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
    DEBUG=os.getenv('DEBUG',False)

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_ECHO=False