"""hours = input("Enter hours: ")
rate = input("Enter hourly rate: ")

try:
  hours = int(hours)
  rate = int(rate)
except:
  print("Error")


overtime = hours % 40
regular = hours - overtime

answer = regular * rate + overtime * 1.5 * rate

print("pay: ", answer) 

nums = [2,34,5,67,89]
max = nums[0]
for num in nums:
    if num>= max:
        max = num
print(max)  


hours = float(input("Enter hours: "))
rate = float(input("Enter hourly rate: "))

def computepay(hours, rate):
 
  overtime = hours % 40
  regular = hours - overtime
  answer = regular * rate + overtime * 1.5 * rate
  return answer

print(computepay(hours, rate))

radius = float(input("enter radious: "))
pi = 3.14159
def area():
    answer = pi * radius**2
    return answer
print( "area = " , area())  """
    

"""
def depending(number):
    
    if number % 4 == 0:
      check = int(input("enter second number: "))
      if number % check == 0:
          return "devided"
      else:
          return "Not divided"  
        
    else:
        return "goodbye"
number = int(input("enter number: "))    
print(depending(number)) """



"""number = int(input("enter number: "))

def depending(num1,numn2):
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(depending())

    
number = "555"
type(number)
dir(number) 
    
s = "banana"

dir(s)
print(dir(s))
result = s.startswith("b")
print(result) 

for i in range(1,101):
    num = str(i)
    if (i % 3 == 0 and i % 5 == 0) and ('3' in num):
        print("FizzBuzzFizz")
    elif (i % 3 == 0 and i % 5 == 0) and ("5" in num):
        print("FizzBuzzBuzz")
    elif (i % 5 == 0) and ("5" in num  and "3" in num):
        print("FizzBuzzBuzz")
    elif (i % 5 == 0) and ("5" in str(i)):
        print("BuzzBuzz")
    elif (i % 3 == 0) and ("3" in str(i)):
        print("FizzFizz")
    elif ("5" in num)  and ("3" in num):
        print("FizzBuzz")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)

print("\nGood Job") """



 
"""a = int(input("enter your number: "))
b = []
for i in range(1, a+1):
  if a % i == 0 and i not in b:
    b.append(i)

print("All the divisors of this number: ", b)"""


"""a = int(input("enter your number: "))
b = []
def find_divisors(a, b):
    for i in range(1, a + 1):
        if a % i == 0 and i not in b:
            b.append(i)
    return b
print(find_divisors(a,b)) 
    
def check(b):     
  if len(b) < 3:
        return "This is prime number."
  else:
        return "This is composite number."

print(check(b))
"""





    
# FizzBuzz Task
"""
def fizzbuzz(x):
    final = ""
    if x % 3 == 0:
        final += "fizz"
    if '3' in str(x):
        final +="fizz"
    if x % 5 == 0:
        final += "buzz"
    if "5" in str(x):
        final += "buzz"
    if len(final) == 0:
        return str(x)
    else:
        return final 
    
for x in range(1, 101):
    print(fizzbuzz(x))

    
print("\nGood Job") 

"""# Part 1.
# int(input("enter your number: "))
"""b = []
for i in range(1, a+1):
  if a % i == 0 and i not in b:
    b.append(i)

print("All the divisors of this number: ", b)"""

"""# Part 2

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Part 1 to help you (as function). Take this opportunity to practice using functions, described below.
"""

"""a = int(input("enter your number: "))
def find_divisors(a, b):
    b = []
    for i in range(1, a + 1):
        if a % i == 0 and i not in b:
            b.append(i)
    return b
b = find_divisors(a,b)

def check(b):
  if len(b) <= 2:
    return "This is prime number."

  else:
    return "This is composite number."


print(check(b))"""

# create phone 

# question_dict = { 
#     "help:"      :        "Show this help ",
#     "quit: "     :        "Quit the program ",
#     "add : "      :       "Create a new contact ",
#     "list :"      :       "Show list of all contacts ",
#     "delete: "    :       " Delete single contact ",
#     "edit: "      :       "Edit exiting contact" }

# def print_help():
#     for cmd in question_dict:
#         print(cmd,question_dict[cmd])
    
# #question = input("Enter a command (h for help):  ")

# contact_dict = {
#     "alice"  : 123445,
#     "bob"   : 234545 }

# def print_contact():
#     i=0
#     for cmd in contact_dict:
#         i+=1
#         print(str(i)+". "+str(cmd)+" -  "+str(contact_dict[cmd]))
       
# def add_contact():
#     name = input("Add your contact's name: ")
#     number = input("Add your contact'number: ")
#     contact_dict[name] = number

# def delete_contact():
#     delete = input("Enter this number's name or number: ")
#     if str(delete)  in contact_dict:
#         del contact_dict[delete]
#     return delete
    
# def edit_contact():
#     name = input("Enter contact's number or full name: ")
#     number = input("Enter new number: ")
#     if name in contact_dict:
#         contact_dict[name]= number
    


# while True:
#     question = input("Enter a command (h for help): ")
#     if  question == "h":
#         print_help()

#     elif question == "list":
#         print_contact()

#     elif question == "quit":
#         print("Goodbye!")
#         quit()

#     elif question == "add":
#         add_contact()
#         print_contact()

#     elif question == "del":
        
#         print(delete_contact())
#         print_contact()
#     elif question == "edit":
#         edit_contact()
#         print_contact()


# s = "hELLO wORLD"
# # inbuilt
# print(s.swapcase())






