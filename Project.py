import datetime
from Database import Database

class Project(Database):

	def __init__(self):
		pass

	def insert(self, name, start_at, end_at, amount):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (name, start_at, end_at, amount)
		sql = "INSERT INTO Projects (name, startAt, endAt, amount) VALUES (%s, %s, %s, %s)"

		try:
			self.db_cursor.execute(sql, data)
		except Exception as e:
			print(e)

		last_id = self.db_cursor.lastrowid 
		self.save()
		self.close()
		return last_id

	def get_by_id(self, project_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()
		
		data = (project_id,)
		sql = "SELECT * FROM Projects WHERE id = %s"

		self.db_cursor.execute(sql, data)
		record = self.db_cursor.fetchall() 

		for row in record:
			project_data = {
				'id' : row[0],
				'name' : row[1],
				'start_at' : row[2],
				'end_at' : row[3],
				'amount' : row[4]
			}

		self.close()	
		return project_data

	def delete_by_id(self, project_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (project_id,)
		sql = "DELETE FROM Projects WHERE id = %s"

		self.db_cursor.execute(sql, data)
		
		self.save()
		self.close()