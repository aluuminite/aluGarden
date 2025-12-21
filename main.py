from gridMath import toIndex, toX, toY

plants = [" "] * 100
plants[toIndex(2, 2)] = "W"
counter, money, rounds = 0, 0, 1
vplants = ["W", "P", "C"]


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
            revenue += 8

        #Update the index
        index += 1

    #Add total revenue
    money += revenue


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

    # Display the plant grid UI
    print("-" * 41)  # Top border of the grid
    for i in range(0, 100, 10):  # Loop through rows (assuming grid size 10x10)
        for plant in plants[i:i + 10]:  # Get 10 plants per row
            print("|", plant, end=" ")  # Print plant with separator
        print("|")  # End of row
        print("-" * 41)  # Row separator

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
        print("P gives 8/r")
        newplantType = " "  # Reset type if rules were requested

    # Assign new plant to the list at the correct index
    plants[toIndex(newplantX, newplantY)] = newplantType.upper()


# Mainloop
while counter < 15:

    update()
    addPlant()
    if rounds % 7 == 0:
        print("Second Turn, round%7 == 0")
        addPlant()
    rounds += 1
