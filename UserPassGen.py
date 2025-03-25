#User&PassGen.py is a script that makes a username based off your name and gives you a random password
#  _   _                        ___     ____                         ____                                    
# | | | |  ___    ___   _ __   ( _ )   |  _ \    __ _   ___   ___   / ___|   ___   _ __        _ __    _   _ 
# | | | | / __|  / _ \ | '__|  / _ \/\ | |_) |  / _` | / __| / __| | |  _   / _ \ | '_ \      | '_ \  | | | |
# | |_| | \__ \ |  __/ | |    | (_>  < |  __/  | (_| | \__ \ \__ \ | |_| | |  __/ | | | |  _  | |_) | | |_| |
#  \___/  |___/  \___| |_|     \___/\/ |_|      \__,_| |___/ |___/  \____|  \___| |_| |_| (_) | .__/   \__, |
#                                                                                             |_|      |___/
#█▄▄ █▄█ ▀  █░█░█ █▄█ ▄▀█ ▀█▀ ▀█▀ █▀▄ ▄▀█ █░░
#█▄█ ░█░ ▄  ▀▄▀▄▀ ░█░ █▀█ ░█░ ░█░ █▄▀ █▀█ █▄▄

from graphics import*

def main():

    win = GraphWin("Username & Password Generator", 800,500)
    win.setCoords(0,0,20,20)

    image = Image(Point(10,10), "UI4Password.gif").draw(win)

    version = Text(Point(19,.5), "v1.0").draw(win)
    version.setSize(9)

    fullName = Entry(Point(13.85,12.5), 17).draw(win)
    fullName.setSize(18)
    fullName.setFill("white")

    win.getMouse()

    fullName.undraw()
    image.undraw()
    newImage = Image(Point(10,10), "UI4PasswordAfter.gif").draw(win)
    
    import random
    import string

    char_set = string.ascii_uppercase + string.digits
    passWord = (''.join(random.sample(char_set*8, 8)))

    fullName = fullName.getText()
    userName = fullName.split()

    first = userName[0][0]
    last = userName[1][0:4]
    userName = first + last

    status = Text(Point(13.85,12.5), "Success!" ).draw(win)
    status.setSize(15)

    userNameText = Text(Point(11.84,9.69), str(userName)).draw(win)
    userNameText.setSize(15)

    passWordText = Text(Point(12.5,6.9), str(passWord)).draw(win)
    passWordText.setSize(15)

    win.getMouse()
    win.close()
    
main()
    
