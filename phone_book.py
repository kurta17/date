# create phone 

question_dict = { 
    "help:"      :        "Show this help ",
    "quit: "     :        "Quit the program ",
    "add : "      :       "Create a new contact ",
    "list :"      :       "Show list of all contacts ",
    "delete: "    :       " Delete single contact ",
    "edit: "      :       "Edit exiting contact" }

def print_help():
    for cmd in question_dict:
        print(cmd,question_dict[cmd])
    
#question = input("Enter a command (h for help):  ")

contact_dict = {
    "alice"  : 123445,
    "bob"   : 234545 }

def print_contact():
    i = 0
    sorted_contacts = sorted(contact_dict.items())
    for name, number in sorted_contacts:
        i += 1
        print(str(i) + ". " + name + " - " + str(number))
       
def add_contact():
    name = input("Add your contact's name: ")
    number = input("Add your contact'number: ")
    contact_dict[name] = number

def delete_contact():
    delete = input("Enter this number's name or number: ")
    if str(delete)  in contact_dict:
        del contact_dict[delete]
    return delete
    
def edit_contact():
    name = input("Enter contact's number or full name: ")
    number = input("Enter new number: ")
    if name in contact_dict:
        contact_dict[name]= number
    


while True:
    question = input("Enter a command (h for help): ")
    if  question == "h":
        print_help()

    elif question == "list":
        print_contact()

    elif question == "quit":
        print("Goodbye!")
        quit()

    elif question == "add":
        add_contact()
        print_contact()

    elif question == "del":
        
        print(delete_contact())
        print_contact()
    elif question == "edit":
        edit_contact()
        print_contact()

