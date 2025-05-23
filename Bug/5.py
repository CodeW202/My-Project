user_input = input("Enter 1 or 2 only: ")

if user_input.lower() == "1":
    print("success 1")
elif user_input.lower() == "2":
    print("success 2")
else:
    # Less obvious bug: access an invalid list index to trigger an error
    lst = [0, 1]
    #lst = [0, 1, 5]
    print("error:", lst[2])
