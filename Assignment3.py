'''
working_hr=int(input('Enter hours worked:'))
if working_hr >40:
    print('Overtime')
elif working_hr >=20 and working_hr <=40:
    print('Normal')
else:
    print('Underworked')
'''


'''
#Use a for loop to print all employee names.

emp_list=['Sujith','Mani','Cheruku','Chintu']
for emp in emp_list:
    print(emp)
'''

#Use a while loop to repeatedly ask for a task until the user types ""done"".

while True:
    task=input('Enter task:')
    if task == 'done':
        print('ThankYou :)')
        break
    else:
        print('Task is Done')

