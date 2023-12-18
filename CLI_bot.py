
def input_error(*type_args):
    def args_parser(func):
        def wrapper(args):

            if len(type_args) != len(args):
                if len(type_args) == 2:
                    return "Give me name and phone please"
                elif len(type_args) == 1:
                    return "Enter user name"
                return "Incorrect arguments amount"

            for i in range(len(type_args)):
                args[i] = type_args[i](args[i])
            try:
                res = func(*args)
            except TypeError as err:
                print(f"Error: {err}")
                res = None
            except ValueError as err:
                print(f"Handler error: {err}")
                res = None
            except KeyError as err:
                print(f"Handler error: {err}")
                res = None
            except IndexError as err:
                print(f"Handler error: {err}")
                res = None

            return res
        return wrapper
    return args_parser


@input_error(str, int)
def add_handler(name, number):
    Contacts[name] = number
    return f"Add name:{name} phone number:{number}"


@input_error()
def hello_handler():
    return "How can I help you?"


@input_error(str, int)
def change_handler(name, number):
    Contacts[name] = number
    return f"Change name:{name}, phone number:{number}"


@input_error(str)
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

        if Comands.get(handler_name) is not None:
            print(Comands[handler_name](args))
        else:
            print("No such command")


if __name__ == "__main__":

    Comands = {
        "hello": hello_handler,
        "add": add_handler,
        "change": change_handler,
        "phone": phone_handler,
    }
    Contacts = {}

    main()
