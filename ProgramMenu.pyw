#ProgramMenu.py is a menu to run a batch of other python programs

from graphics import* #Graphics.py (Allows to open window)

#defining setJustify() to call it on our Text instance (This is because it is in the code of graphics not able to call since it is missing)
def setJustify(self, option):
    if not option in ["left", "center", "right"]:
        raise GraphicsError(BAD_OPTION)
    self._reconfig("justify", option)

def error():

        #Window
        win = GraphWin("Error", 800,500)
        win.setCoords(0,0,20,20)

        message = Text(Point(10,10), """
        Program finished/ or was not selected
        Click to restart program launcher""").draw(win)
        message.setSize(20)

        win.getMouse()

        win.close()

        menu()
        
def menu():

    #Window
    win = GraphWin("Program Menu", 800,500)
    win.setCoords(0,0,10,10)

    message = Text(Point(3.5,9.5), "Enter the number of what program you want:").draw(win)
    message.setSize(20)
    n = Entry(Point(7.5, 9.5), 5).draw(win) #Number determines what story you have.
    n.setText("0")
    n.setFill("white")
    
    #Story options
    options = Text(Point(2,8.5), """
    1. Mad Libs
    2. Number Guessing Game""").draw(win)

    setJustify(options, "left")

    #verison type
    notice = Text(Point(5,.1), "Version 1.0").draw(win)
    notice.setSize(9)
    
    box = Rectangle(Point(6,6),Point(9,9)).draw(win)
    start = Text(Point(7.5,7.5), "Start").draw(win)

    win.getMouse()

    start.setText("Are you sure?")

    win.getMouse()

    n = int(n.getText())

    win.close()

    if n == 1:

        import MadLibsGenerator

    if n == 2:

        import NumberGuessingGame

    else:

        #Error Screen
        error()

menu()
