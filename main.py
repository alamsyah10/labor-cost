import datetime

from Project import Project
from User import User
from Assignment import Assignment
from Database import Database

# 1 people work 8h a day
# 人日単価 one person's cost per day
# if his labor cost 1.000 JPY a day
# 人日単価 is 1.000 JPY
# 稼働率 = 稼働 (work) + 率 (%)
# if certain people's 稼働率 is 50%, it's person work 4h a day

# 人日単価 is the cost when the target person works for one day
# 稼働率 is percentage of working hours that the target person devotes to the target project
# For example, if you are involved in a project for 8 days and the 稼働率 is 50%, you will actually work for 4 days


def calculate_assignment_labor_cost(assignment):
	operating_ratio = assignment['rate']
	user_cost_one_day = User().get_by_id(assignment['user_id'])['amount']
	assignment_days = calculate_assignment_days(assignment['start_at'], assignment['end_at'])
	actual_assignment_days = calculate_actual_assignment_days(assignment_days, operating_ratio)
	assignment_labor_cost = calculate_labor_cost(user_cost_one_day, actual_assignment_days)
	return assignment_labor_cost

def total_labor_cost(assignments):
	assignment_labor_cost = []
	for assignment in assignments:
		assignment_labor_cost.append(calculate_assignment_labor_cost(assignment))

	return sum(assignment_labor_cost)

def labor_cost_percentage(data):
	project_budget = data[0]
	labor_cost = data[1]

	return (labor_cost/project_budget)*100

def calculate_assignment_days(start_at, end_at):
	return (end_at - start_at).days + 1 	#add 1 because the result not including end_at

def calculate_labor_cost(user_cost_one_day, actual_assignment_days):
	return user_cost_one_day * actual_assignment_days

def calculate_actual_assignment_days(assignment_days, operating_ratio):
	return assignment_days * operating_ratio



# tentukan project yang akan dihitung labor costnya
# lakukan assignment pada user dan project tersebut
# ambil data pada database Assignment, berdasarkan id project yang akan dihitung labor costnya
# masing-masing assignment, dapat diambil data: id user, total hari, dan rate nya.
# masing-masing user, dapat diambil data : amount nya.
