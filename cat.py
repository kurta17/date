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
      
 
def encrypt_caesar(msg, shift):
    new_msg = ""
    for i in msg:
        shifted = ord(i) + shift  - ord('A')
        shifted %= 26  
        encrypted_char = chr(shifted + ord('A'))  
        new_msg += encrypted_char
       

    return new_msg


plaintext = "HELLO"
shift_value = 3
encrypted_text = encrypt_caesar(plaintext, shift_value)
print("Encrypted Message:", encrypted_text)
