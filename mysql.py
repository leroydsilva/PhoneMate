from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor





mysql = MySQL(cursorclass=DictCursor,pool_size=5, 
              pool_recycle=3600)


'''
this file is where mysql is initialized so that it can be used by both Phone.py and app.py as a part of namespace.
Else this mysql could have been initialized in app.py.
'''