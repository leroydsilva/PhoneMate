#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
import json
from mysql import mysql
from logging import Formatter, FileHandler
from wtforms import TextField, BooleanField
from flask.helpers import send_from_directory
import os
# from flask_mysqldb import MySQL
from flask_restx import Api

from Phone import phone_ns
from flask_cors import CORS,cross_origin
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
def create_app(config):
    app = Flask(__name__, static_url_path='/',static_folder='./frontend/build')
    app.config.from_object(config)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'flask'

    mysql.init_app(app)
    api=Api(app,doc='/docs')
    api.add_namespace(phone_ns)
    CORS(app)

    @app.route('/')
    @cross_origin()
    def index():
        return send_from_directory(app.static_folder,'index.html')

    @app.errorhandler(404)
    def not_found_error(error):
        app.send_static_file('index.html')

    @app.shell_context_processor
    def make_shell_context():
        return {
            "mysql":mysql
        }

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
