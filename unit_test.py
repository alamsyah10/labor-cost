from faker import Faker
from Project import Project
from User import User
from Assignment import Assignment
from Database import Database
from main import total_labor_cost, labor_cost_percentage
import datetime


def test_project_1():
	assignment = Assignment().get_by_project_id(1)
	labor_cost = total_labor_cost(assignment)
	assert 18340.0 == labor_cost, "Should be 18340.0"

def test_project_2():
	user_data = [
		['dummy_email_123@gmail.com', 12500],
		['dummmy_email_333@gmail.com', 13500],
		['email_email_0@gmail.com', 15000],
		['email_1@gmail.com', 11500],
		['last_email@gmail.com', 13000]
	]
	occupancy_rate = [0.9, 0.75, 0.6, 0.65, 0.8]	# 稼働率
	project_data = ['Big Project XYZ', '2022-06-23', '2022-10-11', 5000000]

	list_of_user_id = insert_user_data(user_data)
	project_id = insert_project_data(project_data)

	assignment_data = set_assignment_data(list_of_user_id, project_id, occupancy_rate)
	list_of_assignment_id = insert_assignment_data(assignment_data)

	assignment = Assignment().get_by_project_id(project_id)
	labor_cost = total_labor_cost(assignment)
	
	delete_inserted_data(list_of_user_id, project_id, list_of_assignment_id)

def test_project_3():
	assignment = Assignment().get_by_project_id(55)
	labor_cost = total_labor_cost(assignment)
	
	assert 676825.0 == labor_cost, "Should be 676825.0"	

def test_project_4():
	# Preparing Data
	user_data = [
		['abcdefg@gmail.com', 10000],
		['rarirurero@gmail.com', 8000],
		['master_programming@gmail.com', 15000]
	]
	occupancy_rate = [1, 0.8, 0.9]
	project_data = ['Transport App', '2022-07-27', '2022-10-25', 5500000]

	list_of_user_id = insert_user_data(user_data)
	project_id = insert_project_data(project_data)

	assignment_date = [
		{'start_at' : '2022-07-30', 'end_at' : '2022-10-20'},
		{'start_at' : '2022-08-03', 'end_at' : '2022-10-22'},
		{'start_at' : '2022-07-27', 'end_at' : '2022-10-10'}
	]
	iteration = 0
	assignment_data = []
	for user_id in list_of_user_id:
		assignment_data.append([project_id, user_id, assignment_date[iteration]['start_at'], assignment_date[iteration]['end_at'], occupancy_rate[iteration]])
		iteration += 1
	list_of_assignment_id = insert_assignment_data(assignment_data)

	# Get data Assignment from database to calculate the labor cost
	assignment = Assignment().get_by_project_id(project_id)

	labor_cost = total_labor_cost(assignment)

	delete_inserted_data(list_of_user_id, project_id, list_of_assignment_id)
	assert 2374400.0 == labor_cost, "Should be 2.374.400"

def create_random_date(start_date, end_date):
	fake = Faker()
	return fake.date_between(start_date = start_date, end_date = end_date)

def insert_user_data(user_data):
	list_of_user_id = []
	for data in user_data:
		list_of_user_id.append(User().insert(data[0], data[1]))
	return list_of_user_id

def insert_project_data(project_data):
	return Project().insert(project_data[0], project_data[1], project_data[2], project_data[3])

def set_assignment_data(list_of_user_id, project_id, occupancy_rate):
	iteration = 0
	assignment_data = []
	for user_id in list_of_user_id:
		fake_start_date = create_random_date(datetime.date(2022, 6, 23), datetime.date(2022, 10, 11))
		fake_end_date = create_random_date(fake_start_date, datetime.date(2022, 10, 11))
		
		assignment_data.append([project_id, user_id, fake_start_date, fake_end_date, occupancy_rate[iteration]])
		iteration += 1
	return assignment_data

def insert_assignment_data(assignment_data):
	list_of_assignment_id = []
	for data in assignment_data:
		list_of_assignment_id.append(Assignment().insert(data[0], data[1], data[2], data[3], data[4]))
	return list_of_assignment_id

def delete_inserted_data(list_of_user_id, project_id, list_of_assignment_id):
	for user_id in list_of_user_id:
		User().delete_by_id(user_id)
	Project().delete_by_id(project_id)
	for assignment_id in list_of_assignment_id:
		Assignment().delete_by_id(assignment_id)



test_project_1()
test_project_2()
test_project_3()
test_project_4()
print("everything passed")