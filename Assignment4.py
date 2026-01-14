'''
#Function: calculate_pay(hours, rate)
#Return total pay.

def calculate_pay(hours, rate):
    total_pay =hours*rate
    return total_pay
print(calculate_pay(2,15))
'''


'''    
#Function: employee_statistics(hours_list)
#Return max, min, and average hours.

def employee_statistics(hours_list):
    max_hr=max(hours_list)
    min_hr=min(hours_list)
    average_hr=sum(hours_list)/len(hours_list)
    return f'maximum hours is {max_hr} minimum hours is {min_hr} and the average hours is {average_hr}'

hours_list=[1,2,3,4,5,6,7,8,9,10]
print(employee_statistics(hours_list))
'''


'''
#Function: search_employee(employees, emp_id)
#Return employee details if found, otherwise ""Employee not found"".yield

def search_employee(employees,emp_id):
    for emp in employees:
        if emp['id']==emp_id:
            return emp
    return 'Employee Not Found'

employees=[
    {'id':10,'name':'sujith','role':'data engineer'},
    {'id':11,'name':'mani','role':'developer'},
    {'id':12,'name':'cheruku','role':'tester'}
    ]
emp_id=15
print(search_employee(employees,emp_id))
'''
