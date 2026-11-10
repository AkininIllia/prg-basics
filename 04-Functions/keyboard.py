###
# Functions to read any data type from the keyboard
#
def input_string(message):
    message = input(message)
    return message

def input_integer(message):
    message = input(message)
    return int(message)

def input_real(message):
    message = input(message)
    return float(message)

def input_boolean(message):
    message = input(message)
    return bool(message)