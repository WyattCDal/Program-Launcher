#NumberGuessingGame.py is a programe that makes that makes the user guess a random number.

from graphics import*
from random import*

def main():

    win = GraphWin("Number Guessing Game", 800, 500)
    win.setCoords(0,0,20,20)

    title = Text(Point(10,19), "Number Guessing Game").draw(win)

    guess = Entry(Point(10, 10), 25).draw(win)
    guess.setText("Enter Number 1-100")

    
    number = randint(1, 100)

    win.getMouse()
    
    if number == guess:

        right = Text(Point(10, 8), "You got it right!").draw(win)

    else:

        wrong = Text(Point(10,8), """You got it wrong.
The number was: """+ str(number)).draw(win)

    win.getMouse()

    win.close()

main()
