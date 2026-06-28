stateA = input("Enter State of Room A: ").strip().lower()
stateB = input("Enter State of Room B: ").strip().lower()

utilityA = int(input("Enter Utility of Room A: "))
utilityB = int(input("Enter Utility of Room B: "))

if stateA == "clean" and stateB == "clean":
    print("No Operation")

elif stateA == "dirty" and stateB == "clean":
    print("Cleaning Room A")
    stateA = "clean"

elif stateA == "clean" and stateB == "dirty":
    print("Cleaning Room B")
    stateB = "clean"

elif stateA == "dirty" and stateB == "dirty":

    if utilityA > utilityB:
        print("Cleaning Room A")
        stateA = "clean"

    elif utilityB > utilityA:
        print("Cleaning Room B")
        stateB = "clean"

    else:
        print("Both rooms have equal utility")
        print("Cleaning Room A")
        stateA = "clean"

print("\nUpdated States:")
print("Room A =", stateA)
print("Room B =", stateB)