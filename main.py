from gridMath import toIndex, toX, toY
import turtle

plants = [" "] * 100
plants[toIndex(2, 2)] = "W"
counter, money, rounds = 0, 0, 1
vplants = ["W", "P", "C"]
SIZE = 64
ROWS = 10
COLS = 10
color_map = {
    "W": "yellow",      # wheat
    "P": "goldenrod",   # potato
    "C": "orange"       # carrot
}

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def toIndex(x, y):
    return (y - 1) * 10 + (x - 1)
def toX(index):
    return index%10+1
def toY(index):
    return index//10+1
def index_to_position(index):
    row = index // 10
    col = index % 10

    start_x = -COLS * SIZE / 2
    start_y = ROWS * SIZE / 2

    x = start_x + col * SIZE
    y = start_y - row * SIZE

    return x, y


def get_int_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                print("Input cannot be empty. Please enter a number.")
                continue
            return int(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_str_input(prompt):
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
            if plants[index+1] == "P" or plants[index-1] == "P" or plants[index+10] == "P" or plants[index-10] == "P":
                revenue += 10

        #Carrot
        if plant == "C":
            revenue += 6+1*rounds

        #Potato
        if plant == "P":
            revenue += 0

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

    x, y = index_to_position(0)

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

            t.color(color_map.get(plants[_]))

            t.penup()
            t.goto(index_to_position(_+1))

            t.begin_fill()
            for ___ in range(4):
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
                newplantX = get_int_input("New Plant X, e.g. 3:")

                # Check if input is in the allowed range
                if newplantX < 11 and newplantX > 0:
                    xcheck = True
                else:
                    print("Input coords 1-10")

            # Get valid Y coordinate
            while ycheck == False:
                newplantY = get_int_input("New Plant Y, e.g. 3:")

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
            newplantType = get_str_input("New Plant type, e.g. W")

            # Check if plant type is valid
            if newplantType.upper() in vplants:
                tcheck = True
            else:
                print("You have to choose one of these plants: ", vplants)

    # Check if user requested rules instead of a plant type
    if newplantType == "Rules":
        print("W gives 10/r and an extra 10 if round%3==0 and there is atleast 1 adjacent potato")
        print("C gives 7/r + 1 per completed round")
        print("P gives 0/r")
        newplantType = " "  # Reset type if rules were requested

    # Assign new plant to the list at the correct index
    plants[toIndex(newplantX, newplantY)] = newplantType.upper()


# Mainloop
while counter < 15:

    update()
    draw()
    addPlant()
    if rounds % 7 == 0:
        print("Second Turn, round%7 == 0")
        draw()
        addPlant()
    rounds += 1
