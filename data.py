counter, money, rounds = 0, 0, 1
vplants = ["W", "P", "C", "A", "B", "V"]
SIZE = 64
ROWS = 10
COLS = 10
prompt = """CLASSIC for classic mode (15 Rounds and double-planting on R7 & R14
            SHORT for short mode (10 Rounds, double-planting)
            INSANE for insane mode (15 Rounds, always double planting)
            MARATHON for marathon mode (30 Rounds, planting every second round)"""

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
