stateA = input("Enter State of Room A: ").strip().lower()
stateB = input("Enter State of Room B: ").strip().lower()

current_location = "A"

if current_location == "A":

    if stateA == "dirty":
        print("Cleaning Room A")
        stateA = "clean"   # Memory Update

    elif stateB == "dirty":
        print("Move to Room B")
        current_location = "B"

        print("Cleaning Room B")
        stateB = "clean"   # Memory Update

    else:
        print("No Operation")

elif current_location == "B":

    if stateB == "dirty":
        print("Cleaning Room B")
        stateB = "clean"   # Memory Update

    elif stateA == "dirty":
        print("Move to Room A")
        current_location = "A"

        print("Cleaning Room A")
        stateA = "clean"   # Memory Update

    else:
        print("No Operation")

print("\nUpdated States:")
print("Room A =", stateA)
print("Room B =", stateB)