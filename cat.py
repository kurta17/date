"""filename = input("Enter your File name: ") or __file__


a = open(filename,"r")
counter = 1
for line in a:
    line = line.rstrip()
    line = line.ljust(80)
    counter += 1
    print(line, "#", counter) """
"""def counter(words): 
    for line in words:
        words = words.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
        return words

counter(counts)"""


"""filename = input("Enter your File name: ") or __file__
file = open(filename, "r")
counts = {}


for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print(counts)

bigword = 0
bigcount = 0

for word,count in counts.items():
    if bigcount == 0 or count > bigcount:
        bigcount = word
        bigcount = count

print(bigcount, bigword)"""


# def fizzbuzz(x):
#     final = ""
#     if x % 3 == 0:
#         final += "fizz"
#     if '3' in str(x):
#         final +="fizz"
#     if x % 5 == 0:
#         final += "buzz"
#     if "5" in str(x):
#         final += "buzz"
#     if len(final) == 0:
#         return str(x)
#     else:
#         return final 
    
# for x in range(1, 101):
#     print(fizzbuzz(x))

    
# print("\nGood Job") 
      
 
question_dict = {
    "help:": "Show this help ",
    "quit:": "Quit the program ",
    "add:": "Create a new contact ",
    "list:": "Show list of all contacts ",
    "delete:": "Delete single contact ",
    "edit:": "Edit existing contact"
}

def print_help():
    for cmd in question_dict:
        print(cmd, question_dict[cmd])

contact_dict = {
    "alice": 123445,
    "bob": 234545
}

def print_contact():
    i = 0
    sorted_contacts = sorted(contact_dict.items())
    for name, number in sorted_contacts:
        i += 1
        print(str(i) + ". " + name + " - " + str(number))

def add_contact():
    name = input("Add your contact's name: ")
    number = input("Add your contact's number: ")
    contact_dict[name] = number

def delete_contact():
    delete = input("Enter this name or number to delete a contact: ")
    if delete in contact_dict:
        del contact_dict[delete]
        return delete
    else:
        return None

def edit_contact():
    name = input("Enter contact's name or number to edit: ")
    if name in contact_dict:
        number = input("Enter new number: ")
        contact_dict[name] = number

while True:
    question = input("Enter a command (h for help): ")
    if question == "h":
        print_help()
    elif question == "list":
        print_contact()
    elif question == "quit":
        print("Goodbye!")
        quit()
    elif question == "add":
        add_contact()
        print_contact()
    elif question == "delete":
        deleted_contact = delete_contact()
        if deleted_contact:
            print(f"{deleted_contact} has been deleted.")
        else:
            print("Contact not found.")
        print_contact()
    elif question == "edit":
        edit_contact()
        print_contact()

        

