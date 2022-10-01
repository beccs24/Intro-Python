def print_main_menu(main_menu):
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


def is_numeric(val):
    """
    Returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    for i in range(len(val)):
        x = val.count('.')
        if x > 1 or (val[i] != '.' and val[i].isdigit() == False):
            return False
    return True

            
def create_category(info):
    """
    Given a string `info`, which is supposed to
    contain the category name and its percentage,
    return a two-element list, which contains this
    information stored as a string d a float
    respectively. 
    Calls is_numeric() to verify
    that the percentage is a numeric value (int or float).
    Stores the percentage as a float (not as a string).
    
    E.g., if the input is "Quiz 25", the function
    returns a list:    ["Quiz", 25.0]
    If splitting the `info` string does not result
    in a two-element list, then return -2.   
    If the last input value (the percentage) in `info`
    is not numeric (int or float), does not update the
    list and returns -1 instead.
    """    
    split_info = info.split()
    if len(split_info) == 2:
        ele1 = split_info[0]
        if is_numeric(split_info[1]) == True:
            ele2 = float(split_info[1])
            return [ele1, ele2]
        else:
            return -1
    else:
        return -2


def print_categories(main_list):
    """
    Given a list of lists, for each list
    stored in main_list, output its contents
    as follows: f"{item[0]} - {item[1]}%".
    If `main_list` is empty, the function prints
    "There are no categories."
    Returns the number of categories.
    """
    num_categories = len(main_list)
    if len(main_list) == 0:
        print("There are no categories.")
    else:
        for i in range(len(main_list)):
            print(f'{i+1}. {main_list[i][0]} - {main_list[i][1]}%')
            
    return num_categories


def is_valid_index(idx, in_list):
    """
    Checks whether the provided index `idx`
    is a valid positive index that can retrieve
    an element from `in_list`.
    Returns False if `idx` is negative or exceeds
    the size of `in_list`.
    """
    if idx >= 0 and idx < len(in_list):
        return True
    else:
        return False


def update_category(info_str, idx, main_list):
    """
    Given a string with the category information
    and an integer index of the category
    that needs to be updated in the list of lists.

    Call is_valid_index(idx, main_list)
    to check the validity of the index;
    returns -3 if `idx` is negative or exceeds
    the size of `in_list`.

    Call create_category(info_str) to
    add the category to the main list;
    returns the result of calling create_category(),
    which is a list if the update succeeds or an
    integer indicating an error.
    """
    if is_valid_index(idx, main_list) == False:
        return -3
    else:
        update = create_category(info_str)
        return update


def create_grade_list(grade_info):
    """
    grade_info : a string of grades, space separated, e.g., "90 98 88"
    return: 
        -1  : if any grade in the string is not numeric
        Otherwise, return a list of float grades    
    """
    split_grade_info = grade_info.split()
    new_list = []
    for i in range(len(split_grade_info)):
        if is_numeric(split_grade_info[i]) == False:
            return -1
        else:
            new_list.append(float(split_grade_info[i]))
    return new_list


def sum_grades(all_categories):
    avg_sum = 0
    for category in all_categories:  #go through each category list in all_categories
        grade_sum = 0
        if len(category) == 2: # if a category only has a name and weight, but no list of grades, then treat it as not
   # having any grades for that category, in which case you add 0 to avg_sum and move onto the next category
           avg_sum += 0
        else:
            for grade in category[2]: #go through the grades list as added in 2nd index of category list
                grade_sum += grade
            if len(category[2]) != 0:
                avg_sum += (grade_sum / len(category[2])) * (category[1] / 100)
            else:
                avg_sum += 0

    return avg_sum



if __name__ == "__main__":
    the_menu = {"P" : "Print categories",
                "A" : "Add a category",
                "U" : "Update a category",
                "G" : "Add grades",
                "C" : "Compute the grade",
                "Q" : "Quit this program"}
    
    all_categories = [] # store the records for each individual category (the list of lists)

    opt = None

    while True:
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")

        if opt == 'A': 
            while True:
                print("Enter the category name and percentage: ")
                cat_info = input()
                cat_list = create_category(cat_info)
                if type(cat_list) == list:
                    all_categories.append(cat_list)
                else: # returned an int error
                    print("WARNING: invalid category information!")
                    print(f"Category information `{cat_info}` was not added.")
                print("Enter another category? Enter 'y' to continue.")
                user_option = input()
                if user_option != 'y':
                    break
            print('*************************')
            print(f'Stored categories: {all_categories}')

        elif opt == 'P': 
            print_categories(all_categories)
            
        elif opt == 'U':
            print_categories(all_categories)
            print("Which category would you like to update?")
            print("Enter the number corresponding to the category.")
            user_option = input()
            if not user_option.isdigit():
                print(f"WARNING: `{user_option}` is an invalid category number!")
            else:
                idx = int(user_option) - 1
                if not is_valid_index(idx, all_categories):
                    print(f"WARNING: `{user_option}` is an invalid category number!")
                else:
                    print(f"Updating category {all_categories[idx][0]}")
                    print("Enter the category name and percentage: ")
                    cat_info = input()
                    cat_list = create_category(cat_info)
                    if type(cat_list) == list:
                        all_categories[idx] = cat_list
                    else:
                        print("WARNING: invalid category information!")
                        print(f"Category information `{cat_info}` was not added.")

        elif opt == 'G':
            print_categories(all_categories)
            print("To which category would you like to add grades?")
            print("Enter the number corresponding to the category.")
            user_option = input()
            if not user_option.isdigit():
                print(f"WARNING: `{user_option}` is an invalid category number!")
            else:
                idx = int(user_option) - 1
                if not is_valid_index(idx, all_categories):
                    print(f"WARNING: `{user_option}` is an invalid category number!")
                else:
                    print(f"Adding grades to category {all_categories[idx][0]}")
                    print("Enter the numeric grades separated by spaces: ")
                    grade_info = input()
                    grade_list = create_grade_list(grade_info)
                    if type(grade_list) == list:
                        if len(all_categories[idx]) == 2:
                            # if no grades for this category have been added
                            print("Adding new grades")
                            all_categories[idx].append(grade_list)
                        else:
                            # there are already grades stored, add the new ones
                            print("Updating the grades")
                            all_categories[idx][2] += grade_list
                        print("-" * 45)
                        print("Category:", all_categories[idx][0]) 
                        print("Grades:", all_categories[idx][2]) 
                        print("-" * 45)
                    else:
                        print("WARNING: invalid grade information!")
                        print(f"The grade data `{grade_info}` was not added.")
                        
        elif opt == 'C':
            avg_grade = sum_grades(all_categories) 
            print(f"Average Grade is: {avg_grade}")

        elif opt == "Q" or opt == "q": 
            print("Goodbye!")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid": 
                print(f"WARNING: `{opt}` is an invalid option.\n")
                # print("This option is not yet implemented.")
                continue
            print(f"You selected option `{opt}` to {the_menu[opt]}.")
            


        #if opt == 'L': # note that the menu should store the keys as strings
        #    # print_categories(all_categories)
        #    pass # TODO 5: remove the pass; define the function, uncomment to call it
        #else:
        #    print("This option is not yet implemented.") # TODO: implement the rest of the options

        opt = input("::: Press Enter to continue...")
        

    print("See you next time!")
