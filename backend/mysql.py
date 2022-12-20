from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)
'''
this file is where mysql is initialized so that it can be used by both Phone.py and app.py as a part of namespace.
Else this mysql could have been initialized in app.py.
'''