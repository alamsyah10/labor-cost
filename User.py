from Database import Database

class User(Database):

	def __init__(self):
		pass

	def insert(self, email, amount):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (email, amount)
		sql = "INSERT INTO Users (email, amount) VALUES (%s, %s)"

		try:
			self.db_cursor.execute(sql, data)
		except Exception as e:
			print(e)

		last_id = self.db_cursor.lastrowid 
		self.save()
		self.close()
		return last_id

	def get_by_id(self, user_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()
		
		data = (user_id,)
		sql = "SELECT * FROM Users WHERE id = %s"

		self.db_cursor.execute(sql, data)
		record = self.db_cursor.fetchall() 

		for row in record:
			user_data = {
				'id' : row[0],
				'email' : row[1],
				'amount' : row[2]
			}

		self.close()	
		return user_data


	def delete_by_id(self, user_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (user_id,)
		sql = "DELETE FROM Users WHERE id = %s"

		self.db_cursor.execute(sql, data)
		
		self.save()
		self.close()
