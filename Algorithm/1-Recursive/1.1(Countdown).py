'''
Differences Between Recursive and Iterative Implementations
Memory Usage:
Recursive: Each recursive call adds a new frame to the call stack. For large values of n, this can lead to high memory usage or even stack overflow.
Iterative: Uses a single loop with constant memory, making it more efficient for large counts.
Performance:
Recursive: In languages without tail-call optimization, recursion has overhead from repeated function calls.
Iterative: Typically faster because it avoids the overhead of many function calls.
Readability:
Recursive: Can be elegant and easier to understand for simple problems.
Iterative: Often considered more straightforward for simple countdown tasks, especially in imperative languages.
Tail-Call Optimization:
In some languages that support tail-call optimization, a recursive solution can be as efficient as an iterative one—but this isn’t universal.
Both approaches solve the problem, but for a basic countdown, the loop is generally preferred due to its lower overhead and simpler memory usage.
'''

#Countdown from 5
n = 5


#Recursive
function countdown(n):
    if n <= 0:
         print("Time's up!")
         return
    print(n)
    countdown(n - 1)




#iterative
function countdown(n):
    for i from n down to 1:
         print(i)
    print("Time's up!")



#Both are iterative and efficient

#For
for i from n down to 1:
    print(i)
print("Time's up!")


#While
i = n
while i > 0:
    print(i)
    i = i - 1
print("Time's up!")
