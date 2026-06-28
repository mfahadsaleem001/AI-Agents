state = input("Enter a State: ").strip().lower()

if state == "dirty":
    print("Cleaning!")
elif state == "clean":
    print("Moving!")
else:
    print("Invalid Input!")