while True:
    x = input("Enter a number: ")
    if x == "exit":
        print("Exiting the program.")
        break
    try:
        x = int(x)
        print(f"You entered: {x}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")