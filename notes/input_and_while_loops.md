# Input and While Loops

### `input()` Function
`input()` function is used when we want to get input from the user. `input()` function will pause the program to allow user to enter the requested input. Once the requested input is received, Python will run the rest of the program.
```python
message = input("Tell me anything, and I will echo it to you: ")
print(message)
```
To write longer prompts for `input()` function, we can assign prompts to a variable which we can later add additional information if we want.
```python
prompt = "You will be asked to enter some of your personal information."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello {name}")
```

### Using `int()` to Accept Numerical Input
By default, Python treats input received from `input()` function as strings. So if we want to receive numerical value from the user for instance their age, Python will interpret it as a string value.<br>
If we try to apply mathmatical operations on the raw input, we will get `TypeError` error as we cannot add number to a string.<br>
To fix this we should write `input()` function inside the `int()` function which will convert the given value to integer.
```python
age = int(input("How old are you? "))

if age >= 18:
    print("You can enter the building")
```
### The Modulo Operator
The modulo operator is represented as `%` symbol in Python. It is a useful tool for working with numerical information; it divides one number by another and returns the remainder.<br>
We can use modulo operator to write a program in order to detect whether the number entered is even or odd.
```python
number = int(input("Enter a number to see if it's even or odd: "))

if number % 2 == 0:
    print("The number is even.")
elif number % 2 != 0:
    print("The number is odd.")
```

### `while` Loops
The difference that `while` loops have compared to the `for` loops is the `for` loops execute a block of code for each item in a collection (lists and dictionaries) whereas `while` loops run as long as a certain condition is `True`.
```python
current_number = 1

while number <= 5:
    print(current_number)
    current_number += 1
```

### Letting the User Choose When to Quit
Most of the programs we use in our day-to-day lifes use `while` loops. One of the common ways to use `while` loops is to run a program until the user wants to quit.
```python
prompt = "Enter 'quit' to end the program."
prompt += "\nTell me anything, and I will echo it to you: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

### Using a Flag
In previous examples, as long as the condition defined in the `while` loop was `True`, the loop executed its code block and when it was `False` Python stoped executing the `while` loop. But in bigger programs there can be several ways to stop a program. For example, in a simple game, when you die, run out of supplies, or the time runs out, the game should end. All of these conditions should break the `while` loop, but this is not possible to do in conditional-based `while` loops. Instead we should use a flag to determine whether a `while` loop should execute or not. In this way several conditions could modify the flag in order to stop Python from executing the `while` loop.
```python
prompt = "Enter 'quit' to end the program."
prompt += "\nTell me anything, and I will echo it to you: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

### Using `break` to Exit a Loop
In order to exit from a `while` loop immediately without running code in the loop, regardless of the results of any conditional test, use the `break` statement.<br>
The `break` statement gives you control over your program, allowing you to direct its flow. You can determine what and when your code should execute.
```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to the {city.title()}")
```

### Using `continue` in a Loop
We can use `continue` statement to return to the beginning of the loop based on the result of a conditional test instead of breaking it entirely.<br>
For instance, we will only print odd numbers using `continue` statement.
```python
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
```

### Moving Items from One List to Another Using `while` Loop
Moving through a list using a `for` loop cause Python lose track of the postion it is in and it will skip some of the items in the list. To fix this issue, we should use while loop to go through and modify a list or dictionary.
```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
```

### Removing All Instances of Specific Values from a List
As discussed `remove()` method removes items according to their value. We can run a `while` loop over a list to make sure a specific value being is removed through out a list.
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

### Filling a Dictionary with User Input
Using `while` loops, you can prompt as much input as you want. In this case we will save the information in a dictionary.
```python
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ")
    response = input("What is your favorite programming language: ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/ n): ")
    if repeat.lower() == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} loves {response} programming language.")
```