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
  new_task = input('Input what task you wanna add')
  task_type = input('Is it recurring or just random (reccuring/random)')
  failing = input('What happens if you do not complete it withen the set time')
  if task_type == ("recurring").upper:
    day_of_week = input('what dayhis event end')
    time_of_task = input('What ti/days of the weeks does this event occur on? Monday, Tuesday, Wednesday...')
    end_time = input('when does tmes is this task due/start at?')
    task = {
      'day_of_week':day_of_week,
      'name' : new_task,
      'task_type' : task_type,
      'time_of_task' : time_of_task,
      'end_time' : end_time,

  }
  elif task_type == 'random':
    difficulty = input('How difficult is it on a scale of 1-10')
    prioridy = input('On a scale of 1-10, should it go first or last?')
    due_date = input('what is the due date? Format:MM/DD/YYY')      
    dictionary = {
      'penalty_for_failing' : failing,
      'difficulty' : difficulty,
      'prioridy' : prioridy,
      'due_date' : due_date
    }              




  # due date
  # penalty for failing
  # reward
  # what percent is done
  # priority 
  # time it takes/ diffuculty 
  # recurring or random:
  #   how often per































def save_task(task_list):
  with open(file_name, 'w') as file


