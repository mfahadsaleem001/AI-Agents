stateA = input("Enter State of Room A: ").strip().lower()
stateB = input("Enter State of Room B: ").strip().lower()

goal = "both rooms clean"

while not (stateA == "clean" and stateB == "clean"):

    if stateA == "dirty":
        print("Cleaning Room A")
        stateA = "clean"

    elif stateB == "dirty":
        print("Moving to Room B")
        print("Cleaning Room B")
        stateB = "clean"

print("Goal Achieved!")
print("Room A: ", stateA)
print("Room B: ", stateB)