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


def validate_name(name):
    '''
    Validates the "name" parameter
    Returns True if the name is between 3 and 15 characters long, inclusive
    and does not contain any commas.
    Returns False otherwise
    '''
    if 3 <= len(name) <= 15:
        if ',' in name:
            return False
        else:
            return True
    else:
        return False


def validate_description(desc):
    '''
    Validates the "desc" parameter
    Returns True if desc is a non-empty string
    and does not contain any commas.
    Returns False otherwise
    '''
    if len(desc) > 0:
        if ',' in desc:
            return False
        else:
            return True
    else:
         return False


def validate_date(date_string):
    '''
    Validates the "date_string"
    Returns True if date_string is a valid date string
    in slashes format (lab 8.16)
    Returns False otherwise
    '''
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    my_tokens = date_string.split('/')
    if len(my_tokens) == 3:
        if my_tokens[0].isdigit() and my_tokens[1].isdigit() and my_tokens[2].isdigit():
            if 1 <= int(my_tokens[0]) <= 12:
                if 1 <= int(my_tokens[1]) <= num_days[int(my_tokens[0])]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validate_priority(priority):
    '''
    Validates the "priority" parameter
    Returns True if "priority" is a string containing a number 1-5
    Returns False otherwise
    '''
    if priority == '1' or priority == '2' or priority == '3' or priority == '4' or priority == '5':
        return True
    else:
        return False


def validate_completed(comp):
    '''
    Validate the "comp" parameter.
    Returns True if "comp" is one of: "yes", "no", "Yes", "No"
    Returns False otherwise
    '''
    if comp == "yes" or comp == "no" or comp == "Yes" or comp == "No":
        return True
    else:
        return False
