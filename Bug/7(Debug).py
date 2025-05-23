import pdb

valid_inputs = ["1", "2", "3"]
user_input = input("Enter 1, 2, or 3 only: ")

if user_input.lower() in valid_inputs:
    if user_input.lower() == "1":
        print("success 1")
    else:
        print("success 2")
else:
    pdb.set_trace()  # Drop into the debugger here
    lst = [0, 1]
    print("error:", lst[2])

'''
You can debug it like any other Python error. Here are some techniques:

Examine the traceback: When you trigger the error (for example by entering an invalid input like "4"), Python will print a traceback that shows where the error occurred. This tells you that the error happens when trying to access lst[2] in your else block.
Use a debugger (pdb): You can insert pdb.set_trace() right before the error line to inspect variables and step through your code. For example:

When you run this and input an invalid value (like "4"), execution will pause at pdb.set_trace(). You can then use commands like p to print variable values or n to step to the next line to see exactly what’s happening.
Print statements: Insert temporary print statements to check the values of variables (e.g., print out user_input and valid_inputs) before the error line. This is a simple but effective way to trace the program flow.
Using these methods, you can determine why the error occurs and how the code is reaching that point. Remember, in this example the error is intentionally triggered for demonstration purposes. In a production setting, you’d typically handle invalid input more gracefully (for example, by reprompting the user) rather than causing a runtime error.
'''