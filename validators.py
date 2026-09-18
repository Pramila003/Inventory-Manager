def get_non_empty(promt):
    while True:
        value = input(promt).strip()

        if value != "":
            return value
        else:
            print("This field can not be empty")


def get_valid_number(promt, number_type, minimum):
    while True:
        try:
            value = number_type(input(promt))
            if value <minimum :
                print("number must be at least", minimum)
                continue
            return value
        
        except ValueError:
            print("enter the valid number")


def validate_email(email):
    if "@" not in email:
        return False

    at_position = email.index("@")
    if "." not in email[at_position:]:
        return False

    return True

def confirm_action(message):
    while True:
        
        answer = input(message + "(yes/no)").lower().strip()
        if answer == 'yes':
            return True

        if answer =='no':
            return False

        print("please enetr yes or no")
        confirm_action
        

