

def input_error(func):
    def wrapper(args):
        if func == add_handler:
            print(f"Error: {func}")
        try:
            res = func(*args)
        except TypeError as err:
            print(f"Error: {err}")
            res = None
        except ValueError or KeyError or IndexError as err:
            print(f"Handler error: {err}")
            res = None

        return res
    return wrapper



@input_error
def add_handler(name,number):
    Contacts[name] = number
    return f"Add name:{name} phone number:{number}"


@input_error
def hello_handler():
    return "How can I help you?"


@input_error
def change_handler(name,number):
    Contacts[name] = number
    return f"Change name:{name}, phone number:{number}"


@input_error
def phone_handler(name):
    number = Contacts[name]
    return f"Phone number:{number}"



def main():

    while True:

        user_input = input(">>> ")
        user_input = user_input.lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "show all":
            print(Contacts)
            continue

        items = user_input.split(" ")
        handler_name, *args = items

        if Comands[handler_name](args) is not None:
            print(Comands[handler_name](args))


if __name__ == "__main__":

    Comands = {
        "hello": hello_handler,
        "add": add_handler,
        "change": change_handler,
        "phone": phone_handler,
    }
    Contacts = {}

    main()
