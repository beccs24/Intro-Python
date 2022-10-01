from tasks import *
from extra_credit import *


if __name__ == "__main__":
    the_menu = {'P': 'Print tasks',
                'A': 'Add a task',
                'U': 'Update a task',
                'D': 'Delete a task',
                'SI': 'Show incomplete tasks',
                'SC': 'Show completed tasks',
                'SP': 'Show tasks sorted by priority, highest first',
                'SD': 'Show tasks sorted by deadline, earliest first',
                '*': 'Show tasks sorted alphabetically by name',
                'S': 'Save tasks',
                'L': 'Load tasks from file',
                'Q': 'Quit this program'}
    
    all_tasks = [] # store the records for each individual task (the list of dictionaries)

    opt = None

    while True:
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")


        if opt.lower() == 'p': # .lower() allows string input to be capital letters
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            if len(all_tasks) == 0:
                print("There are no tasks currently!")
            else:
                print_formatted_tasks(all_tasks)
            
        elif opt.lower() == 'a': 
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print_formatted_tasks(all_tasks)
            
            name = input("Input name: ")
            description = input("Input description: ")
            date = input("Input date: ")
            priority = input("Input priority: ")
            completion = input("Input completion: ")
            
            result = create_a_task(name, description, date, priority, completion)
            all_tasks.append(result[1]) # adds each new task into a list of all tasks
            print_formatted_tasks(all_tasks)
            
        elif opt.lower() == 'u':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print_formatted_tasks(all_tasks)

            task_id = int(input("Which task number would you like to update? "))
            task_field = input("Which field would you like to update? ")
            task_update = input("What would you like to update to? ")
            
            update_result = update_task(all_tasks, task_id, task_field, task_update)
            all_tasks[task_id] = update_result[1]

            print_formatted_tasks(all_tasks)

        elif opt.lower() == 'd':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print_formatted_tasks(all_tasks)

            idx = int(input("Which task number would you like to delete? "))
            
            if delete_task(idx, all_tasks) == False:
                print("Invalid index.")
            else:
                print_formatted_tasks(all_tasks)
        
        elif opt.lower() == 'si':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))

            not_done = [] # list that stores all tasks that are False for completed field

            for i in range(len(all_tasks)):
                if all_tasks[i]['completed'] == False:
                    not_done.append(all_tasks[i])

            print_tasks_by_status(not_done, False)

        elif opt.lower() == 'sc':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))

            done = [] # list that stores all tasks that are True for completed field

            for i in range(len(all_tasks)):
                if all_tasks[i]['completed'] == True:
                    done.append(all_tasks[i])

            print_tasks_by_status(done, True)
               
        elif opt.lower() == 'sp': # EXTRA CREDIT OPTION
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print_sorted_priority(all_tasks)
                
        elif opt.lower() == 'sd': # EXTRA CREDIT OPTION
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print_sorted_deadline(all_tasks)

        elif opt == '*': # EXTRA CREDIT OPTION
            print("You selected option {} to > {}.".format(opt, the_menu[opt]))
            print_sorted_alphabetically(all_tasks)
            
        elif opt.lower() == 's':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            filename = input("What would you like to save your filename as? ")
            save_to_csv(all_tasks, filename)
        
        elif opt.lower() == 'l':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            filename1 = input("What is the filename you would like to load? ")
            
            if not os.path.exists(filename1): # checks if the filename exists
                print(f'WARNING: Cannot find a CSV file named {filename1}.')
            else:
                load_from_csv(filename1)
                # print(load_from_csv(filename1))
            
        elif opt.lower() == 'q':
            print("You selected option {} to > {}.".format(opt, the_menu[opt.upper()]))
            print("See you next time!")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid": 
                print("This option is not yet implemented.") 
            # print(f"You selected option {opt} to > {the_menu[opt.upper()]}.")
            

        opt = input("::: Press Enter to continue...")

    print("Have a productive day!")
    

