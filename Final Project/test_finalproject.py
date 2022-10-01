from tasks import *

# ASSERT TESTS FOR VALIDATE FILE
# test check_option function
my_menu0 = {}
my_menu1 = {1: "One"}
my_menu2 = {'L': "List"}

result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`\n")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu2)
print(f"--> check_option('1', my_menu2) returned `{result}`\n")
assert result == "invalid"

result = check_option('L', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "valid"

result = check_option('l', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "invalid"


# test is_valid_index function
assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True


# test is_numeric function
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5')
print(f"--> is_numeric('5.5') returned `{result}`")
assert result == True

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False


# test validate_name function
assert validate_name('hi,') == False
assert validate_name('hi') == False
assert validate_name('books') == True


# test validate_description function
assert validate_description('y,es') == False
assert validate_description('good') == True
assert validate_description("") == False


# test validate_date function
assert validate_date('5/10/23') == True
assert validate_date('13/24/15') == False
assert validate_date('04/14/2022') == True


# test validate_priority function
assert validate_priority('4') == True
assert validate_priority('1.0') == False
assert validate_priority(1.0) == False
assert validate_priority(10) == False


# test validate_completed function
assert validate_completed('yes') == True
assert validate_completed(False) == False
assert validate_completed('True') == False


# ASSERT TESTS FOR TASKS FILE
# test check_option function
my_menu0 = {}
my_menu1 = {1: "One"}
my_menu2 = {'L': "List"}

result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`\n")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu2)
print(f"--> check_option('1', my_menu2) returned `{result}`\n")
assert result == "invalid"

result = check_option('L', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "valid"

result = check_option('l', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "invalid"


# test create_a_task function
# Regular input 1
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[0] == True
assert type(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]) == dict
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['name'] == 'do dishes'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['description'] == 'wash the plates from dinner'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['deadline'] == '03/04/2022'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'] == 2
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'] == False

# Regular input 2
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[0] == True
assert type(create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]) == dict
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['name'] == 'see endgame'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['description'] == 'endgame with friends saturday'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['deadline'] == '01/18/2020'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['priority'] == 3
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['completed'] == True

# name too short
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[1] == 'name'

# name too long
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[1] == 'name'

# description empty
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[1] == 'description'

# invalid dates empty
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[1] == 'deadline'

# invalid priority
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[1] == 'priority'

# invalid completion
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[1] == 'completed'


# test slashes_to_written function
assert slashes_to_written(["01", "02", "2022"]) == 'January 2, 2022'
assert slashes_to_written(["01", "12", "1970"]) == 'January 12, 1970'
assert slashes_to_written(["04", "14", "2020"]) == 'April 14, 2020'
assert slashes_to_written(["06", "19", "2000"]) == 'June 19, 2000'


# test update_task function
my_list = [{
        'name': 'get groceries',
        'description': 'buy some jam and peanut butter',
        'deadline': '02/23/2022',
        'priority': 2,
        'completed': False
        },
        {
        'name': 'get some sleep',
        'description': '8 hours of sleep is necessary',
        'deadline': '02/03/2022',
        'priority': 3,
        'completed': True
        },
        {
        'name': 'compar. lit essay',
        'description': "finish comparative lit essay that's overdue",
        'deadline': '02/15/2022',
        'priority': 4,
        'completed': True
        }]

result = update_task(my_list, 5, 'name', 'go clubbing')
assert result[1] == "idx"
assert result[0] == False
print(f"--> update_task(my_list, 5, 'name', 'go clubbing') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'Get Gift', 'I\'m quite hungry though')
assert result[1] == "field"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'Get Gift', 'I\'m quite hungry though') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'deadline', 'never')
assert result[1] == "deadline"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'deadline', 'never') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'priority', 'pants on FIRE!!!!')
assert result[1] == "priority"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'priority', 'pants on FIRE!!!!') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'completed', 'technically, yes')
assert result[1] == "completed"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'completed', 'technically, yes') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'Deadline', '01/22/19')
assert result[0] == True
assert result[1]['deadline'] == '01/22/19'
print(f"--> update_task(my_list, 1, 'Deadline', '01/22/19' "+
      f"successfully returned updated task: \n{result[1]}\n")

result = update_task(my_list, 1, 'Completed', 'no')
assert result[0] == True
assert result[1]['completed'] == False
print(f"--> update_task(my_list, 1, 'Completed', 'no') "+
      f"successfully returned updated task: \n{result[1]}\n")

print(">>All assertions successfully run...\n")


# test delete_task function
assert delete_task(2, []) == False
assert delete_task(1, ['hi', 'sup']) == True
