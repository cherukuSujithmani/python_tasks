#Ask the user for hours worked and handle if input is invalid.

#hours_worked=float(input())
'''
try:
    hours_worked=float(input())
    print(hours_worked)
except ValueError:
    print('working hours should be number')
  '''  

#Create safe_productivity_score(tasks_completed, hours_worked)function:
#Score = tasks_completed / hours_worked
#Return an appropriate message when an error occurs.

def safe_productivity_score(tasks_completed, hours_worked):
    try:
        Score = tasks_completed / hours_worked
        return f'No Errors Score is :{Score}'
    except ZeroDivisionError :
        return 'working hours should not be 0'
    except TypeError:
        return 'task_completed or working hours should be number'


try:
    tasks_completed=int(input('enter no of task completed:'))
    hours_worked=float(input('enter working hours:'))
    print(safe_productivity_score(tasks_completed, hours_worked))
except ValueError:
    print('Error: Please enter valid numeric values')


