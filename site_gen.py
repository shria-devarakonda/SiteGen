name = input("Enter is your name: ")
desc = input("Enter your description: ")
script = "<!DOCTYPE html> <html> <head> <style> h1 {text-align: center;} p {text-align: center;} </style> </head> <body style=\"background-color:blueviolet;\"> <font color = \"#FF00CB\" face = \"Comic sans MS\" size = \"7\"><br /> <h1>"
script2 = name + "</h1> <p>" + desc + "</p> </font> </body> </html>"
with open(name + "spage.html", "w+") as f:
        f.write(script + script2)
