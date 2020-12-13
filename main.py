import requests, os

# Add the attributes.
class Attribs():
  __creators__ = "Diary & Annuals"
  __version__ = "1.2.1"
  __usage__ =  "input username"
  __repl__ = "https://repl.it/@Diary/GitHub-Username-Checker#main.py"


print("""
 ________  ___  _________  ________  ___  ___  _______   ________  ___  __    _______   ________     
|\   ____\|\  \|\___   ___\\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \___|\ \  \|___ \  \_\ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \   \ \  \ \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \   \ \  \ \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\   \ \__\ \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|    \|__|  \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|
                                                                                                     
                                                                                                     
""")

class Check():
  username = input("GitChecker - The free to use GitHub Username Checker\n\nInput your username.\nC:/GitChecker/github.py> ")
  web = requests.get(f"https://api.github.com/users/{username}")
  check = requests.get(f"https://api.github.com/users/{username}")

  if web.status_code == "404":
    print("Username " + username + " is available.")
  else:
    print(f"Username {username} is not available.")