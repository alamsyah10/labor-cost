import mysql.connector

class Database:
	def __init__(self):
		pass	

	def connect(self):
		self.my_db = mysql.connector.connect(
			host = 'localhost',
			user = 'root',
			password = '',
			database = 'dummy_db'
		)

	def save(self):
		self.my_db.commit()

	def close(self):
		self.my_db.close()