# config.py
db = {
    'user'     : 'root',		# 1)
    'password' : '0000',		# 2)
    'host'     : 'localhost',	# 3)
    'port'     : 3306,			# 4)
    'database' : 'tromm'		# 5)
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"