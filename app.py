#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
import json
from logging import Formatter, FileHandler
# from wtforms import TextField, BooleanField
from flask.helpers import send_from_directory
import os
# from flask_mysqldb import MySQL
from flask_restx import Api
from models import db
# from mysql import mysql
from flask_cors import CORS,cross_origin

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
def create_app(config):
    app = Flask(__name__,)
    api=Api(app,doc='/docs')
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    
    # mysql.init_app(app)
    CORS(app)
    db.init_app(app)
    # db.reflect()
    from Phone import phone_ns
    api.add_namespace(phone_ns)
    

    @app.route('/')
    def index():
        return "yo bro"


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    return app


# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


# @app.route('/')
# def home():
#     return render_template('pages/placeholder.home.html')



# @app.route('/about')
# def about():
#     return render_template('pages/placeholder.about.html')


# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)


# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)


# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)

# Error handlers.


# @app.errorhandler(500)
# def internal_error(error):
#     # db_session.rollback()
#     return render_template('errors/500.html'), 500





# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter(
#             '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
