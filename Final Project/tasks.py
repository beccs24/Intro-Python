from validate import *

def print_main_menu(main_menu):
    '''
    Given a main_menu dictionary, this function prints the main menu in a specific format.
    '''
    print("*" * 26)
    print("What would you like to do?")
    for key, action in main_menu.items():
        print(f'{key} - {action}')
    print("*" * 26)


def check_option(option, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided collection.
    Otherwise, return "invalid".
    """
    if (type(option) == str) and (option in menu):
        return "valid"
    else:
        return "invalid"


def create_a_task(name, description, date, priority, completion):
    '''
    Calidate each parameter starting from "name" and until "completion"
    If one of them fails, return (False, <name of parameter>)
    ex. (False, "name") if "name" is not 3-15 characters long
    or (False, "completion") if completion is not a "yes" or "no"
    If all validations pass, return (True, <dictionary with fields name, description...>)
    '''
    if validate_name(name) == False:
        return (False, "name")
    elif validate_description(description) == False:
        return (False, "description")
    elif validate_date(date) == False:
        return (False, "deadline")
    elif validate_priority(priority) == False:
        return (False, "priority")
    elif validate_completed(completion) == False:
        return (False, "completed")
    else:
        if completion == "yes" or completion == "Yes":
            complete = True
        else:
            complete = False
        dict = {"name": name,
                "description": description,
                "deadline": date,
                "priority": int(priority),
                "completed": complete
               }
        return (True, dict)


def slashes_to_written(date_list):
    '''
    Given a date list, this function converts and returns a numerical date into a written date. 
    '''
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = month_names[int(date_list[0])]
    if date_list[1][0] == '0':
        day = date_list[1][1]
    else:
        day = date_list[1]
    year = date_list[2]
    date = month + " " + day + ", " + year

    return date


def print_formatted_tasks(tasks_list):
    '''
    Given a task list, this function formats the task list so it can be read easily.
    '''
    for i in range(len(tasks_list)):
        print(f'{i}:  {tasks_list[i]["name"].upper()}')
        print('    Description:', tasks_list[i]["description"])
        if int(tasks_list[i]['priority']) == 1:
            level = "Lowest"
        elif int(tasks_list[i]['priority']) == 2:
            level = "Low"
        elif int(tasks_list[i]['priority']) == 3:
            level = "Medium"
        elif int(tasks_list[i]['priority']) == 4:
            level = "High"
        else: 
            level = "Highest" 
        print('    Priority:', level)
        date_split = tasks_list[i]['deadline'].split("/")
        print('    Deadline:', slashes_to_written(date_split))
        if tasks_list[i]['completed'] == False:
            print('    Completed: No')
        else: 
            print('    Completed: Yes')
        print()


def print_tasks_by_status(all_tasks, completed = False):
    '''
    Prints tasks from 'all_tasks',
    based on the value of 'completed' of each task.
    If there are no tasks that are incomplete,
    prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed,
    prints 'You do not have completed tasks.'
    Otherwise, prints the requested tasks.
    '''
    
    if len(all_tasks) == 0:
        if completed == False:
            print("You do not have incomplete tasks.")
        else:
            print("You do not have completed tasks.")
    else:
        print_formatted_tasks(all_tasks)


def update_task(task_list, task_id, task_field, task_update):
    '''
    This function takes in the task list, a task index, a task field, and the updated information. 
    Parameters will be validated to check for syntax and structure. If all validations are passed, 
    return a tuple containing boolean True and your updated task. if validations fail, return a
    tuple containing 'False' and a string that describes the error from validation.
    '''

    fields = [
    'name',
    'description',
    'deadline',
    'priority',
    'completed'
    ]

    if is_valid_index(task_id, task_list) == False:
        return False, 'idx'

    if task_field.lower() not in fields:
        return False, 'field'

    if task_field.lower() == 'name': 
        if validate_name(task_update) == False:
            return False, 'name'
        else:
            task_list[task_id]['name'] = task_update
            return True, task_list[task_id]
    elif task_field.lower() == 'description':
        if validate_description(task_update) == False:
            return False, 'description'
        else:
            task_list[task_id]['description'] = task_update
            return True, task_list[task_id]
    elif task_field.lower() == 'priority':
        if validate_priority(task_update) == False:
            return False, 'priority'
        else:
            task_list[task_id]['priority'] = task_update
            return True, task_list[int(task_id)]
    elif task_field.lower() == 'deadline':
        if validate_date(task_update) == False:
            return False, 'deadline'
        else:
            task_list[task_id]['deadline'] = task_update
            return True, task_list[task_id]
    elif task_field.lower() == 'completed':
        if validate_completed(task_update) == False:
            return False, 'completed'
        else:
            if task_update == "No" or task_update == 'no':
                task_list[task_id]['completed'] = False
                return True, task_list[task_id]
            else: 
                task_list[task_id]['completed'] = True
                return True, task_list[task_id]


def delete_task(idx, tasks):
    '''
    Checks if idx, which is an integer, is a valid index inside Tasks
    If not, returns False
    If a valid index, removes the element at index 'idx'
    from tasks, and returns True
    '''
    if is_valid_index(idx, tasks) == False:
        return False
    else:
        tasks.pop(idx)
        return True
    

import csv

def save_to_csv(task_list, filename):
    '''
    Given a task_list and its filename, this function
    saves stored the data in the main collection as a csv file.
    '''
    
    with open(filename, 'w', newline='') as filename:
        task_writer = csv.writer(filename)
        for i in range(len(task_list)):
            task_data = list(task_list[i].values())
            task_writer.writerow(task_data)


import os

def load_from_csv(filename):
    '''
    Reads the csv file and creates a new list of tasks using
    the data in that file. Loop through the lines of data and 
    in each iteration, call create_a_task() to get the data 
    as a dictionary. Save each valid dictionary into the list 
    tasks (i.e., dictionaries).
    Note that this function is responsible for converting
    the last (Boolean) field of the task from "True"/"False"
    to "yes"/"no", so that the task can be correctly created
    using the create_a_task() function.

    Return the resulting list of dictionaries, which will be 
    empty, if the file is empty or the data in it is invalid.
    '''
    
    new_list = [] # empty list to store the data from the csv file
    
    with open(filename, 'r') as filename:
        reader_object = csv.reader(filename, delimiter = ',')

        for values in reader_object:
            if len(values) == 5: #check if there are 5 items in the list 'values'
                
                #convert the last field (a Boolean flag) to "yes" or "no"
                if values[4] == 'True':
                    values[4] = "yes"
                elif values[4] == 'False':
                    values[4] = "no"
                
                #call create_a_task and add it to new_list
                result = create_a_task(values[0], values[1], values[2], values[3], values[4]) 

                if result[0] == True:
                    new_list.append(result[1])
                else:
                    print("WARNING: invalid data -", values)
                    return "invalid data"

            else: #if data formatting is inconsistent
                print("WARNING: invalid data -", values)
                print("WARNING: Data formatting is inconsistent with the task manager!")
                return "inconsistent format"

    return new_list
