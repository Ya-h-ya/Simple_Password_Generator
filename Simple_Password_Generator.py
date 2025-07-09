import random
letter_password = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
number_password = ['1','2','3','4','5','6','7','8','9','0']
special_password = ['-','+','=','[',']','#','?',',','.',';',':','@']
combine_lst = letter_password
final_password = []

print("--Welcome to the password generator--")

len_password = int(input("How long will you like your password to be?: "))
numbers = input("do you want numbers?(y/n): ").lower()
symbols = input("do you want symbols?: ").lower()

if numbers == "y":
    combine_lst += number_password

if symbols == "y":
    combine_lst += special_password


for i in range(len_password):
    final_password.append(random.choice(combine_lst))
    

final = "".join(final_password)
print(final)
    




    