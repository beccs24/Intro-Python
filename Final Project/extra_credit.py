from tasks import *

def print_sorted_priority(all_tasks):
    """
    Prints tasks from all_tasks, but sorted by priority,
    highest priority first
    """

    priority_tasks = []
    sorted_pt = []

    for i in range(len(all_tasks)): # add values of each priority field from all tasks
        priority_tasks.append(all_tasks[i]['priority'])

    reversed_pt = sorted(priority_tasks, reverse = True) # sorts values of priority from largest to smallest

    for i in reversed_pt: # 5,3,2,...
        for j in range(len(all_tasks)): # 0,1,2,...
            if all_tasks[j]['priority'] == i:
                sorted_pt.append(all_tasks[j]) # add sorted tasks by priority into new list

    print_formatted_tasks(sorted_pt)


def print_sorted_deadline(all_tasks):
    """
    Prints tasks from all_tasks, but sorted by deadline
    earliest first
    """
    
    deadline_tasks = []
    sorted_deadline = []

    for i in range(len(all_tasks)): # add values of each deadline field from all tasks
        deadline_tasks.append(all_tasks[i]['deadline'])

    sort_deadline = sorted(deadline_tasks) # sorts dates from earliest to latest
    
    for i in sort_deadline: 
        for j in range(len(all_tasks)): 
            if all_tasks[j]['deadline'] == i:
                sorted_deadline.append(all_tasks[j]) # add sorted tasks by date into new list

    print_formatted_tasks(sorted_deadline)


def print_sorted_alphabetically(all_tasks):
    '''
    This function prints tasks from all_tasks, but sorted by the
    name of the task in alphabetical order.
    '''
    
    task_names = []
    sorted_names = []

    for i in range(len(all_tasks)): # add strings of each name field from all tasks
        task_names.append(all_tasks[i]['name'])

    sort_names = sorted(task_names) # sorts name strings in alphabetical order
    
    for i in sort_names: 
        for j in range(len(all_tasks)): 
            if all_tasks[j]['name'] == i:
                sorted_names.append(all_tasks[j]) # add sorted tasks by alphabetical name strings into new list

    print_formatted_tasks(sorted_names)

