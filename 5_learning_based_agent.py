stateA = input("Enter State of Room A: ").strip().lower()
stateB = input("Enter State of Room B: ").strip().lower()

experience = 0

if stateA == "dirty":
    print("Cleaning Room A")
    stateA = "clean"
    experience += 1

if stateB == "dirty":
    print("Cleaning Room B")
    stateB = "clean"
    experience += 1

print("\nUpdated States:")
print("Room A =", stateA)
print("Room B =", stateB)

print("Experience Gained =", experience)

if experience > 0:
    print("Agent learned from its actions.")
else:
    print("No learning occurred.")