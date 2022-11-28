import pygame
from Rectangle import Rectangle
from Surface import Surface

class Login:
  def __init__(self):
    #self.login = ""
    self.username = []
    self.password = []
    self.userpassword_dict = { 
      
    }
    for self.username, self.password in self.userpassword.dict.items():
      self.userpassword.dict = self.userpassword.dict.add(self.username, self.password)
  
  def __str__(self):
    return self.userpassword_dict

  def LoginScreenStrings(self):
    
    self.logintitle = "Login here"
    self.usertitle = "Username:"
    self.passtitle = "Password:"
    self.help = "Click here for help"

  def TextboxInput(self):
    self.usernameInput = #textbox with prompt to input username
    self.passwordInput = #textbox with prompt to input password



#https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
# def LS():
#   loggedin = 0

#   ls = input("Do you want to\n[1] Sign up\n[2] Login\n[3] Continue without login\n")
#   if ls == "1":
#     susername = input("Username:")
#     spassword = input("Password:")
#     db[susername] = spassword
#     print("You are successfully signed up and logged in!")
#   elif ls == "2":
#     username = input("Username: ")
#     password = input("Password: ")
#     allUsernames = db.keys()
#     if username in allUsernames:
#       realpassword = db[username]
#       if password == realpassword:
#        print("Welcome Back!")
#        loggedin = 1
#        time.sleep(1)
#        print()
#        clear()
#       else:
#         print("Password wrong")
#         time.sleep(1)
#         clear()
#     else:
#       print("Sorry! You are not found in are system please sign up!")
#       time.sleep(1)
#       clear()
#   elif ls == "3":
#     loggedin = 0
#     guestusername = "Guest" + str(random.randint(0,10000))
#     print("Your Username is " + guestusername)
#   else:
#     print("Thats not an option!")

# LS()