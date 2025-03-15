#MadLibsGenerator.py is a script that ask the user to input words to create a story.

from graphics import* #Graphics.py (Allows to open window)

#defining setJustify() to call it on our Text instance (This is because it is in the code of graphics not able to call since it is missing)
def setJustify(self, option):
    if not option in ["left", "center", "right"]:
        raise GraphicsError(BAD_OPTION)
    self._reconfig("justify", option)

def main():

    #Window
    win = GraphWin("Mad Libs Generator", 800,500)
    win.setCoords(0,0,10,10)

    message = Text(Point(3.5,9.5), "Enter the number of what story you want:").draw(win)
    message.setSize(20)
    n = Entry(Point(7, 9.5), 5).draw(win) #Number determines what story you have.
    n.setText("0")
    n.setFill("white")
    
    #Story options
    options = Text(Point(2,8.5), """
    1. A Day at the Zoo
    2. The Spooky Haunted House""").draw(win)

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
    
    if n == 1: #A Day at the Zoo

        #Window
        win = GraphWin("A Day at the Zoo", 800,500)
        win.setCoords(0,0,10,10)

        #Title
        message = Text(Point(1.45,9.5), "A Day at the Zoo").draw(win)
        message.setSize(20)

        #Boxes with all the entries
        place1 = Entry(Point(1,8.9), 15).draw(win) 
        place1.setText("(place)")
        place1.setFill("white")

        name1 = Entry(Point(1,8.5), 15).draw(win)
        name1.setText("(name)")
        name1.setFill("white")

        adjective1 = Entry(Point(1,8.1), 15).draw(win)
        adjective1.setText("(adjective)")
        adjective1.setFill("white")

        animal1 = Entry(Point(1,7.7), 15).draw(win)
        animal1.setText("(animal)")
        animal1.setFill("white")

        verb1 = Entry(Point(1,7.3), 15).draw(win)
        verb1.setText("(verb ending in -ing)")
        verb1.setFill("white")

        place2 = Entry(Point(1,6.9), 15).draw(win)
        place2.setText("(place in the zoo)")
        place2.setFill("white")

        number1 = Entry(Point(1,6.5), 15).draw(win)
        number1.setText("(number)")
        number1.setFill("white")

        noun1 = Entry(Point(1,6.1), 15).draw(win)
        noun1.setText("(plural noun)")
        noun1.setFill("white")

        noise1 = Entry(Point(1,5.7), 15).draw(win)
        noise1.setText("(funny noise)")
        noise1.setFill("white")

        adjective2 = Entry(Point(1,5.3), 15).draw(win)
        adjective2.setText("(adjective)")
        adjective2.setFill("white")

        animal2 = Entry(Point(1,4.9), 15).draw(win)
        animal2.setText("(plural animal)")
        animal2.setFill("white")

        food1 = Entry(Point(1,4.5), 15).draw(win)
        food1.setText("(food)")
        food1.setFill("white")

        object1 = Entry(Point(1,4.1), 15).draw(win)
        object1.setText("(object)")
        object1.setFill("white")

        name2 = Entry(Point(1,3.7), 15).draw(win)
        name2.setText("(celebrity name)")
        name2.setFill("white")

        phrase1 = Entry(Point(1,3.3), 15).draw(win)
        phrase1.setText("(funny phrase)")
        phrase1.setFill("white")

        adjective3 = Entry(Point(1,2.9), 15).draw(win)
        adjective3.setText("(adjective)")
        adjective3.setFill("white")

        souvenir = Entry(Point(1,2.5), 15).draw(win)
        souvenir.setText("(souvenir)")
        souvenir.setFill("white")

        adjective4 = Entry(Point(1,2.1), 15).draw(win)
        adjective4.setText("(adjective)")
        adjective4.setFill("white")

        #Comfirm Box
        box = Rectangle(Point(6,6),Point(9,9)).draw(win)
        start = Text(Point(7.5,7.5), "Start").draw(win)

        win.getMouse()

        start.setText("Are you sure?")

        win.getMouse()

        box.undraw()
        start.undraw()

        #Items
        place1 = place1.getText()
        name1 = name1.getText()
        adjective1 = adjective1.getText()
        animal1 = animal1.getText()
        verb1 = verb1.getText()
        place2 = place2.getText()
        number1 = number1.getText()
        noun1 = noun1.getText()
        noise1 = noise1.getText()
        adjective2 = adjective2.getText()
        animal2 = animal2.getText()
        food1 = food1.getText()
        object1 = object1.getText()
        name2 = name2.getText()
        phrase1 = phrase1.getText()
        adjective3 = adjective3.getText()
        souvenir = souvenir.getText()
        adjective4 = adjective4.getText()
        
        #Story
        story = Text(Point(5.8,6.5), " ").draw(win)
        story.setText("""        Today, I went to the """+ str(place1) +""" with my best friend """+ str(name1) +""".
        We saw a huge """+ str(adjective1) +""" """+ str(animal1) +""" that was """+ str(verb1) +""" near the """+ str(place2) +""".
        It had """+ str(number1) +""" """+ str(noun1) +""" on its back, and it made a """+ str(noise1) +""" sound! 

        Next, we fed some """+ str(adjective2) +""" """+ str(animal2) +""". They loved eating """+ str(food1) +""" and even tried to
        steal my """+ str(object1) +"""!
        We laughed so hard that """+ str(name2) +""" turned around and said, """+ str(phrase1) +"""! 

        Before we left, we visited the gift shop and bought a """+ str(adjective3) +""" """+ str(souvenir) +""".
        It was the most """+ str(adjective4) +""" day ever, and I can’t wait to go back!""")
        setJustify(story, "left")

        #Close feature
        close = Text(Point(5,.1), "Click to close window").draw(win)
        close.setSize(9)

        win.getMouse()
        win.close()

    elif n == 2: #The Spooky Haunted House

        # Window
        win = GraphWin("The Spooky Haunted House", 800, 500)
        win.setCoords(0, 0, 10, 10)

        # Title
        message = Text(Point(2.2, 9.5), "The Spooky Haunted House").draw(win)
        message.setSize(20)

        # Boxes with all the entries
        name1 = Entry(Point(1, 8.9), 15).draw(win)
        name1.setText("(name)")
        name1.setFill("white")

        adjective1 = Entry(Point(1, 8.5), 15).draw(win)
        adjective1.setText("(adjective)")
        adjective1.setFill("white")

        street_name = Entry(Point(1, 8.1), 15).draw(win)
        street_name.setText("(street name)")
        street_name.setFill("white")

        adjective2 = Entry(Point(1, 7.7), 15).draw(win)
        adjective2.setText("(adjective)")
        adjective2.setFill("white")

        plural_noun1 = Entry(Point(1, 7.3), 15).draw(win)
        plural_noun1.setText("(plural noun)")
        plural_noun1.setFill("white")

        verb_past1 = Entry(Point(1, 6.9), 15).draw(win)
        verb_past1.setText("(verb, past tense)")
        verb_past1.setFill("white")

        adjective3 = Entry(Point(1, 6.5), 15).draw(win)
        adjective3.setText("(adjective)")
        adjective3.setFill("white")

        sound = Entry(Point(1, 6.1), 15).draw(win)
        sound.setText("(sound)")
        sound.setFill("white")

        room = Entry(Point(1, 5.7), 15).draw(win)
        room.setText("(room in a house)")
        room.setFill("white")

        adjective4 = Entry(Point(1, 5.3), 15).draw(win)
        adjective4.setText("(adjective)")
        adjective4.setFill("white")

        creature = Entry(Point(1, 4.9), 15).draw(win)
        creature.setText("(creature)")
        creature.setFill("white")

        verb_ing = Entry(Point(1, 4.5), 15).draw(win)
        verb_ing.setText("(verb ending in -ing)")
        verb_ing.setFill("white")

        body_part = Entry(Point(1, 4.1), 15).draw(win)
        body_part.setText("(body part, plural)")
        body_part.setFill("white")

        adjective5 = Entry(Point(1, 3.7), 15).draw(win)
        adjective5.setText("(adjective)")
        adjective5.setFill("white")

        object1 = Entry(Point(1, 3.3), 15).draw(win)
        object1.setText("(object)")
        object1.setFill("white")

        exclamation = Entry(Point(1, 2.9), 15).draw(win)
        exclamation.setText("(exclamation)")
        exclamation.setFill("white")

        adjective6 = Entry(Point(1, 2.5), 15).draw(win)
        adjective6.setText("(adjective)")
        adjective6.setFill("white")

        food = Entry(Point(1, 2.1), 15).draw(win)
        food.setText("(food)")
        food.setFill("white")

        verb_past2 = Entry(Point(1, 1.7), 15).draw(win)
        verb_past2.setText("(verb, past tense)")
        verb_past2.setFill("white")

        object2 = Entry(Point(1, 1.3), 15).draw(win)
        object2.setText("(object)")
        object2.setFill("white")

        # Confirm Box
        box = Rectangle(Point(6, 6), Point(9, 9)).draw(win)
        start = Text(Point(7.5, 7.5), "Start").draw(win)

        win.getMouse()

        start.setText("Are you sure?")

        win.getMouse()

        box.undraw()
        start.undraw()

        # Items
        name1 = name1.getText()
        adjective1 = adjective1.getText()
        street_name = street_name.getText()
        adjective2 = adjective2.getText()
        plural_noun1 = plural_noun1.getText()
        verb_past1 = verb_past1.getText()
        adjective3 = adjective3.getText()
        sound = sound.getText()
        room = room.getText()
        adjective4 = adjective4.getText()
        creature = creature.getText()
        verb_ing = verb_ing.getText()
        body_part = body_part.getText()
        adjective5 = adjective5.getText()
        object1 = object1.getText()
        exclamation = exclamation.getText()
        adjective6 = adjective6.getText()
        food = food.getText()
        verb_past2 = verb_past2.getText()
        object2 = object2.getText()

        # Story
        story = Text(Point(5.8, 5), " ").draw(win)
        story.setText("""        Last night, my friend """ + str(name1) + """ and I decided to explore the """ + str(adjective1) +
        """ old house at the end of
        """ + str(street_name) + """.
        People say it's """ + str(adjective2) +
        """ and full of """ + str(plural_noun1) + """!
        As we stepped inside, the door """ + str(verb_past1) + """ behind us. We heard a """ + str(adjective3) +
        """ """ + str(sound) + """
        coming from the """ + str(room) + """.
        Suddenly, a """ + str(adjective4) +
        """ """ + str(creature) + """ jumped out and started """ + str(verb_ing) + """ toward us!
        We ran as fast as our """ + str(body_part) + """ could take us, but then we saw a """ + str(adjective5) +
        """ """ + str(object1) + """
        floating in the air. "This is """ + str(exclamation) + """!" I shouted.
        Just as we thought we were doomed, a """ + str(adjective6) + """ ghost appeared and handed us a """ + str(food) +
        """.
        "Eat this, and you'll be safe," it whispered. We """ + str(verb_past2) + """,
        and suddenly, everything went back to normal.
        I still can't believe that night happened! Next time, I'll bring a """ + str(object2) + """ to protect myself.""")

        setJustify(story, "left")

        # Close feature
        close = Text(Point(5, .1), "Click to close window").draw(win)
        close.setSize(9)

        win.getMouse()
        win.close()

    
    else: #Error Window

        error = GraphWin("No Story Selected", 800,500)
        error.setCoords(0,0,10,10)

        message = Text(Point(5,5), """
        No Story Selected
        Click to restart Mad Libs""").draw(error)
        message.setSize(20)

        error.getMouse()

        error.close()
        
        main()
        
main()
