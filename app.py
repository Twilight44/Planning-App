from flask import Flask, request, jsonify, render_template  
import json
import os
from datetime import timedelta, datetime 





app = Flask(__name__)

file_name = 'tasks.json'



def load_task():
   if os.path.exists(file_name):
        with open(file_name, "r" ) as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[] 
        return[]
    

def save_task(task_list):
   with open(file_name, "w") as file:
      json.dump(task_list, file, indent=4)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/tasks', methods = ["GET"] )
def get_task():
   return jsonify(load_task()) #jsonify is a function that will convert python into a json format 


@app.route('/tasks', methods = ["POST"] )
def add_task():
    data = request.json
    task_list = load_task()
    task_list.append(data)
    save_task(task_list) 
    return jsonify({"status":"sucess"}), 201

if __name__ == "__main__":
    app.run(debug = True)


