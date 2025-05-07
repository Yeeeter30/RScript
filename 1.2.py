# Imports
import os
import time

# Welcome
print("Welcome back to RScript Version 1.2")
name = input("Enter You're name please: ")
print("Hello", name)
print("That is all i needed")

# Choice clear
print("""
1. Clear
2. Skip
""")
choice = input("Enter a choice (1/2): ")
if choice == "1":
    print("Clearing in")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    os.system("clear")
elif choice == "2":
    print("Skipping proceeded")
    pass
    
# Welcome 2
time.sleep(1)
print("Welcome", name, "To RScript")
print("Proceeding...")

# Choice script
print("""
1. test
2. exit
3. AI
""")
choice2 = input("Pick a choice (1/2/3): ")
if choice2 == "1":
    print("test")
    exit()
elif choice2 == "2":
    print("Exiting")
    exit()
elif choice2 == "3":
    print("Welcome", name, "to the RScript AI")
    print("""
1. Male
2. Female
3. Prefer not to say
""")
    gender = input("Pick a Choice (1/2/3): ")
    if gender == "1":
        print("Thanks for confirming youre a Male", name)
        gender2 = "Male"
    elif gender == "2":
        print("Thanks for confirming youre a Female", name)
        gender2 = "Female"
    elif gender == "3":
        print("Thanks for confirming you do not prefer to say", name)
        gender2 = "Prefer not to say"
        
        
# Age
age = input("Enter age please: ")
print("Ok you are", age, "years old?")

# Code end exit
time.sleep(5)
print("Exiting...")
print("Goodbye", name)
