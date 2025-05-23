valid_inputs = ["1", "2", "3"]
user_input = input("Enter 1 or 2 only: ")

if user_input.lower() in valid_inputs:
    if user_input.lower() == "1":
        print("success 1")
    else:  # if it's "2"
        print("success 2")
else:
    # Intentionally trigger an error for invalid input (for demonstration)
    lst = [0, 1]
    print("error:", lst[2])
