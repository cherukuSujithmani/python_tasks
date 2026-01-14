#2.1 create a list of employee dictionaries and add,remove and print the employee list
'''
emp_list=[
          {'emp_id':7,'name':'Dhoni','Dpt':'caption'},
          {'emp_id':45,'name':'Rohit Sharma','Dpt':'caption'}
          ]
#adding new employee
emp_list.append({'emp_id':18,'name':'Virat','Dpt':'Batsmen'})
print(emp_list)#

#removing employee from the list
emp_list.pop() # it will remove the last employee from the list add index number to remove spefic

print(emp_list)
print(len(emp_list))
'''
'''
#2.2 creating a dictinary where are employee ids and values are list

task={
    7:['caption','batsmen'],
    45:['caption','part-time bowler']
    }
task[7].append('finesher')
#print(task)
task[45].remove('part-time bowler')
#print(task)
print(task.values())
#for i,j in task.items():
    #print(f"cricketer's id is {i} tasks:",j)

'''
'''
# 2.3 unique skills using sets

skills={'caption','keeper',}
skills.add('Batsmen')
skills.add('Bowler')
print(skills)
'''

#2.4 company Holidays using tuples

holidays = ("2026-01-01", "2026-01-15", "2026-12-25")
print(holidays)
#holidays.append('20-1-2012')






