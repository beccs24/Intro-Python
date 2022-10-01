from grades_system import *

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


# test create_category function
# Check the incorrect format of the input
assert create_category("Quizzes") == -2
assert create_category("Quizzes 25.5 ignorethis") == -2
assert create_category("Quizzes A") == -1
# Check the correct input returning the proper list
assert create_category("Quizzes 25.5") == ["Quizzes", 25.5]


# test print_categories function
assert print_categories([]) == 0
print()
assert print_categories([["Quizzes", 25.5]]) == 1
print()
assert print_categories([['Exam1', 20.0], ['Exam2', 25.0]]) == 2


# test is_valid_index function
assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True


# test update_category
assert update_category('Exams 80', 1, [['Exam1', 20.0], ['Exam2', 25.0]]) == ['Exams', 80.0]
assert update_category('Exams 80', 0, []) == -3
assert update_category('Exams', 1, [['Exam1', 20.0], ['Exam2', 25.0]]) == -2
assert update_category('Exams t4', 1, [['Exam1', 20.0], ['Exam2', 25.0]]) == -1


# test create_grade_list function
result = create_grade_list("90 99 98")
print(f"--> create_grade_list('90 99 98') returned `{result}`\n")
assert result == [90.0, 99.0, 98.0]

result = create_grade_list("100 A A- B")
print(f"--> create_grade_list('100 A A- B') returned `{result}`\n")
assert result == -1

result = create_grade_list("")
print(f"--> create_grade_list(\"\") returned `{result}`\n")
assert result == []

result = create_grade_list("95.0 90 60")
print(f"--> create_grade_list('95.0 90 60') returned `{result}`\n")
assert result == [95.0, 90.0, 60.0]


# test sum_grades function
all_categories = [
    ["PA", 5, [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]],
    ["CA", 15, [100.0, 100.0, 98.0, 95.0, 0.0, 100.0]],
    ["LA", 25, [100.0, 100.0, 100.0, 5.0, 0.0, 70.0]],
    ["Quiz", 25, []],
    ["Project", 25, []]
]
assert sum_grades(all_categories) == 32.20
all_categories = []
assert sum_grades(all_categories) == 0.00
all_categories = [["PA", 5, [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]]]
assert sum_grades(all_categories) == 4.25
