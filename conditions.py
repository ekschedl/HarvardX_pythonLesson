while True:
    user_input = input("Number or 'stop' for exit: ").lower()
    if user_input == "stop":
        break
    try:
        n= int( user_input)
        if n > 0:
            print("Number is positive")
        elif n < 0:
            print("Number is negative")
        else:
            print("Number is 0")
    except ValueError:
        print("Please enter a valid number or 'stop' to exit.")



