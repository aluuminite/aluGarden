import turtle
from tabnanny import check

from pattern import checkNeighbours, checkAdjacentP, checkUniqueAdjacent
from gridMath import toX, toY, toIndex, indexToPos

SIZE = 64
ROWS = 10
COLS = 10


plants = [" "] * 110
plants[toIndex(3, 3)] = "W"
counter, money, rounds = 0, 0, 1
vplants = ["W", "P", "C", "A", "B"]
SIZE = 64
ROWS = 10
COLS = 10
colorMap = {
    "W": "yellow",      # wheat
    "P": "goldenrod",   # potato
    "C": "orange",      # carrot
    "A": "red",         # apple
    "B": "lime"         # bamboo
}

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def getIntInput(prompt):

    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                print("Input cannot be empty. Please enter a number.")
                continue
            return int(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def getStrInput(prompt):

    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please enter something.")
        else:
            return value

#Calc and apply monetary gains
def update():

    global money
    revenue = 0
    index = 0
    #Run thru plants
    for plant in plants:

        #Wheat
        if plant == "W":
            revenue += 10
            #Check for potatoes
            if checkAdjacentP(plants, index):
                revenue += 6

        #Carrot
        if plant == "C":
            revenue += 6+2*rounds//3

        #Potato
        if plant == "P":
            revenue += 0

        #Apple
        if plant == "A":
            revenue += 15-checkNeighbours(plants, index)*1.5

        if plant == "B":
            revenue += 9+checkUniqueAdjacent(plants, index)*2
        #Update the index
        index += 1

    #Add total revenue
    money += revenue


def gridOD(factor):

    for _ in range(5):
        t.forward(640)
        t.right(90*factor)
        t.forward(64)
        t.right(90*factor)
        t.forward(640)
        t.left(90*factor)
        t.forward(64)
        t.left(90*factor)

def draw():

    t.clear()

    x, y = indexToPos(0, COLS, ROWS, SIZE)

    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    gridOD(1)

    t.forward(640)

    for __ in range(2):
        t.left(90)
        t.forward(640)

    t.left(90)

    gridOD(-1)

    for _ in range(len(plants)):

        if plants[_] != " ":

            t.color(colorMap.get(plants[_]))

            t.penup()
            t.goto(indexToPos(_, COLS, ROWS, SIZE))
            t.setheading(0)
            t.pendown()

            t.begin_fill()
            for _ in range(4):
                t.forward(64)
                t.right(90)
            t.end_fill()

            t.color("black")


# Whole process to add a new plant and display the UI for it
def addPlant():
    global rounds
    # Print current money and round number for reference
    print("$", money, " Round:", rounds)

    # Flags to check if user input is valid
    xcheck = False
    ycheck = False
    tcheck = False
    ccheck = False

    # Loop until valid X, Y, and plant type are chosen
    while xcheck == False or ycheck == False or tcheck == False or ccheck == False:

        while ccheck == False:
            # Get valid X coordinate
            while xcheck == False:
                newplantX = getIntInput("New Plant X, e.g. 3:")

                # Check if input is in the allowed range
                if newplantX < 11 and newplantX > 0:
                    xcheck = True
                else:
                    print("Input coords 1-10")

            # Get valid Y coordinate
            while ycheck == False:
                newplantY = getIntInput("New Plant Y, e.g. 3:")

                # Check if input is in the allowed range
                if newplantY < 11 and newplantY > 0:
                    ycheck = True
                else:
                    print("Input coords 1-10")

            if plants[toIndex(newplantX, newplantY)] == " ":
                ccheck = True
            else:
                print("Choose an empty tile")
                xcheck = False
                ycheck = False

        # Get valid plant type
        while tcheck == False:
            newplantType = getStrInput("New Plant type, e.g. W")

            # Check if plant type is valid
            if newplantType.upper() in vplants:
                tcheck = True
            else:
                print("You have to choose one of these plants: ", vplants)

    # Check if user requested rules instead of a plant type
    if newplantType == "Rules":
        print("W gives 10/r and an extra 6 if there is atleast 1 adjacent potato")
        print("C gives 7/r + 1 per completed round")
        print("P gives 0/r")
        print("A gives more money the further it is from other plants")
        newplantType = " "  # Reset type if rules were requested

    # Assign new plant to the list at the correct index
    plants[toIndex(newplantX, newplantY)] = newplantType.upper()


# Mainloop
while rounds < 16:

    update()
    turtle.tracer(0)
    draw()
    turtle.update()
    addPlant()
    if rounds % 7 == 0:
        print("Second Turn, round%7 == 0")
        turtle.tracer(0)
        draw()
        turtle.update()
        addPlant()
    rounds += 1
