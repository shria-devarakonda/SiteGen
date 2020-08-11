name = input("Enter your name: ")
desc = input("Enter your description: ")
script = "<!DOCTYPE html> <html> <head> <style> h1 {text-align: center;} p {text-align: center;} </style> </head> <body style=\"background-color:blueviolet;\"> <font color = \"#FF00CB\" face = \"Comic sans MS\" size = \"7\"><br /> <h1>"
script2 = name + "</h1> <img src=\"https://i.pinimg.com/originals/b3/e9/9c/b3e99ccfeed46705557e53af6a3307c9.gif\" alt=\"CatPic\" width=\"200\" height=\"300\" align=\"Right\"> <img src=\"https://mir-s3-cdn-cf.behance.net/project_modules/disp/89d8a336589167.57545d7b953e2.gif\" width=\"200\" height=\"300\" alt=\"CatPic\" align=\"Left\"> <p>" + desc + "</p> </font> </body> </html>"
with open(name + "spage.html", "w+") as f:
        f.write(script + script2)
