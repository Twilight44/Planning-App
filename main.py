from datetime import timedelta, datetime 
import json
import os


file_name = "task.json"
def load_task():
  if os.path.exists(file_name):
    with open(file_name,"r") as file:
      return json.load(file)  #load the file with the python format
  return[] #returned an empty list to make sure it doesn't give error and crash because if we return a file that doesn't exist then it crashs

def save_task(task_list):
    with open(file_name, "w" ) as file:
        json.dump(task_list, file, indent = 4) #.dump converts the task list from a python format to json format
    print("task saved succesfully")

def add_task(task_list):
  new_task = input('Input what task you wanna add ').lower()
  task_type = input('Is it recurring or just random (recurring/random) ')
  failing = input('What happens if you do not complete it withen the set time ')
  if task_type == 'recurring': #We can't do recurring.upper because we cannot compare a string(task_type) to a fuction (recurring.upper()) *(recurring).upper is a fuction not a string
    day_of_week = input('what day does event end ')
    time_of_task = input('What days of the weeks does this event occur on? Monday, Tuesday, Wednesday... ')
    end_time = input('when does tmes is this task due/start at ?')
    task = {
     'day_of_week':day_of_week,
      'name' : new_task,
      'task_type' : "recurring",
      'time_of_task' : time_of_task,
      'end_time' : end_time

    }
  elif task_type == 'random':
    difficulty = input('How difficult is it on a scale of 1-10 ')
    priority = input('On a scale of 1-10, should it go first or last? ')
    due_date = input('what is the due date? Format:MM/DD/YYY ')      
    dictionary = {
      'penalty_for_failing' : failing,
      'difficulty' : difficulty,
      'priority' : priority,
      'due_date' : due_date
    }              

  else:
    print("it is an invalid task")

  task_list.append(task)
  print("task succesfully created")

def veiw_tasks(task_list):
  for i,task in enumerate(task_list, start = 1):
    task_type = task.get('task_type')
  if task_type == 'recurring':
    day_of_week = task.get('day_of_week')
    time_of_task = task.get('time_of_task')
    end_time = task.get('end_time')
    print(f'{i}.{task['name']},occurs at{time_of_task}, ends at{end_time} on{day_of_week}')
  elif task_type == 'variable':
    priority = task.get('priority')
    penalty_for_failing = task.get('penalty_for_failing')
    difficulty = task.get('difficulty')
    due_date = task.get('due_date')
    print(f'{i}.{task['name']},is due at{due_date}, is this important{priority}, this will happen if you fail,{penalty_for_failing}, and is this hard{difficulty}')
    
def delete_task(task_list):
  task_deletion = input("What task do you want to delete?").lower().strip()
  task_delete_match = next((task for task in task_list if task_deletion in task["name"]), None) 
  #task_delete_match is list comprehesion that returns a list
 
  if task_delete_match:
    answer = input("Are you sure you want to delete this task? Yes/No ")
    if answer == "Yes":
     task_list.remove(task_delete_match)
     print("Task has been deleted")   
    else:
      print("task deletion canceled")
  
 # def view_schedule(task_list):
def main():
  task_list = load_task() 



  while True:
    print("                                  ")
    print(" Schedule App ")
    print("1. Type Veiw to go view your task ")
    print("2. Type Add to add a task ")
    print("3. Type Delete to delete a task ")
    


    whatever_I_want = input('What do you wanna look at? ').strip()

    if whatever_I_want == 'View':
      veiw_tasks(task_list)
    elif whatever_I_want == 'Add':
      add_task(task_list)
    elif whatever_I_want == 'Delete':
       delete_task(task_list)
    else:
      print("You did something wrong")
      main()

if __name__ == "__main__":
  main()