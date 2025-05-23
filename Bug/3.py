user_input = input("Enter 1 or 2 only: ")

if user_input.lower() == "1":
    print("success 1")
elif user_input.lower() == "2":
    print("success 2")
else:
    # Intentional bug: raise an exception for invalid input.
    raise ValueError("Invalid input! Expected '1' or '2'.")
