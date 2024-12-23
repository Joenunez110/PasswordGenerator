#login project
#*****************************************
#
#  Author : Joe Nunez
#  Date   : 17 Feb 2013
#  Purpose:  To log in, to add users, to log attempts
#
#*****************************************


    
import os
import random
os.chdir(r"C:\Users\Josep\Documents\.vsc")

#greeting

greeting = input("login | signup (l | s): ")

def invalid_input_error():
     print("Invalid input. Please try again.")
     greeting = input("login | signup (l | s): ")



#login
if greeting == "l" or greeting == "L":

    def login():
          username = input("Enter username: ")
          password = input("Enter password: ")
#search for username
          myfile = open("id.txt", "r")
          try:
               while f"{username},{password}" in myfile.read():
                    print("Welcome back", username)
                    break
               else:
                    if f"{username},{password}" not in myfile.read():
                         print("Invalid Credentials.")
                         return login()
                    
          except:
                    print("There seems to be an issue, try again later")
               
    login()

#register

if greeting == "s" or greeting == "S":
    def register():
        # get username and password
        
        username = input("Create username: ")
        password = input("Create password: ")
        password1 = input("Please enter password again: ")
        
        if password != password1:
                print("passwords do not match. Try again.")
                register()
        # check username
        myfile_1 = open("id.txt", "r")
        for lines in myfile_1:
             a, b, c = lines.strip().split(",")
             if username == b:
                  print("Username has been taken, please try again.")
                  return register()
             else:
               a = str(random.randint(000000, 999999))
               for lines in myfile_1:
                  a, b, c = lines.strip().split(",")
                  if a == lines.strip().split(",")[0]:
                       break
                  else:
                       break
        #Format input
        ap = "a,b,c"
        # append to file
        myfile = open("id.txt", "a")
        myfile.write(f"\n{a},{username},{password}")
        print(f"Welcome", (username), "!")
    register()
    
    if greeting != "l" or greeting != "L" or greeting != "s" or greeting != "S":
         invalid_input_error()
