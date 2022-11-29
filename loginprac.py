import os, time, random
from replit import db

def LS():
  loggedin = 0

  ls = input("Do you want to\n[1] Sign up\n[2] Login\n[3] Continue without login\n")
  if ls == "1":
      susername = input("Username:")
      spassword = input("Password:")
      db[susername] = spassword
      print("You are successfully signed up and logged in!")
  elif ls == "2":
      username = input("Username: ")
      password = input("Password: ")
      allUsernames = db.keys()
      if username in allUsernames:
        realpassword = db[username]
        if password == realpassword:
          print("Welcome Back!")
          loggedin = 1
          time.sleep(1)
          print()
          clear()
        else:
          print("Password wrong")
          time.sleep(1)
          clear()
      else:
        print("Sorry! You are not found in are system please sign up!")
        time.sleep(1)
        clear()
  elif ls == "3":
      loggedin = 0
      guestusername = "Guest" + str(random.randint(0,10000))
      print("Your Username is " + guestusername)
  else:
      print("Thats not an option!")

LS()