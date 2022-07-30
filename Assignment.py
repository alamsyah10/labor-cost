import datetime
from Database import Database

class Assignment(Database):

	def __init__(self):
		pass

	def insert(self, project_id, user_id, start_at, end_at, rate):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (project_id, user_id, start_at, end_at, rate)
		sql = "INSERT INTO Assignments (projectId, userId, startAt, endAt, rate) VALUES (%s, %s, %s, %s, %s)"

		try:
			self.db_cursor.execute(sql, data)
		except Exception as e:
			print(e)

		last_id = self.db_cursor.lastrowid 
		self.save()
		self.close()
		return last_id

	def get_by_project_id(self, project_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()
		
		data = (project_id,)
		sql = "SELECT * FROM Assignments WHERE projectId = %s"

		self.db_cursor.execute(sql, data)
		record = self.db_cursor.fetchall() 
		
		assignment_data = []
		for row in record:
			temp_data = {
				'id' : row[0],
				'project_id' : row[1],
				'user_id' : row[2],
				'start_at' : row[3],
				'end_at' : row[4],
				'rate' : row[5]
			}
			assignment_data.append(temp_data) 

		self.close()	
		return assignment_data

	def get_by_id(self, assignment_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()
		
		data = (assignment_id,)
		sql = "SELECT * FROM Assignments WHERE id = %s"

		self.db_cursor.execute(sql, data)
		record = self.db_cursor.fetchall() 

		for row in record:
			project_data = {
				'id' : row[0],
				'project_id' : row[1],
				'user_id' : row[2],
				'start_at' : row[3],
				'end_at' : row[4],
				'rate' : row[5]
			}

		self.close()	
		return project_data

	def delete_by_id(self, assignment_id):
		self.connect()
		self.db_cursor = self.my_db.cursor()

		data = (assignment_id,)
		sql = "DELETE FROM Assignments WHERE id = %s"

		self.db_cursor.execute(sql, data)
		
		self.save()
		self.close()