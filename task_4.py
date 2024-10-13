def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please provide correct arguments."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts():
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts found."


def bot():
    while True:
        command = input("Enter a command: ").lower()
        if command == "add":
            try:
                args = input("Enter name and phone: ").split()
                print(add_contact(args))
            except ValueError:
                print("Give me name and phone please.")
        elif command == "phone":
            try:
                args = input("Enter the name: ").split()
                print(get_phone(args))
            except ValueError:
                print("Enter a valid name.")
        elif command == "all":
            print(show_all_contacts())
        elif command == "exit":
            break
        else:
            print("Unknown command, try again.")


