# If Statements

### A Basic Conditional Code
We can look for specific conditions with `if` conditional codes. `if` conditions either result in `True` or `Flase` values. If the condition is satisfied (`True`), Python runs code block runs. If not (`False`), Python interpreter skips the code block.
```python
car = "bmw"

if car == "bmw":
    print("What a nice car!")
```
- `==` compares and checks the value to see if they are equal or not.

### Using `if` Condition in `for` Loops
We can loop through a list while checking for specific values to perform special operations on them. For example, the code below checks if new users use other variations of previous usernames already registered on the website. Websites make sure that you have a unique username, not just a variation of other registered usernames with different capitalization with this method.
```python
current_usernames = ['mike', 'ninjaprogrammer', 'johnny', 'pythonpro', 'computernerd']

new_usernames = ['john', 'ComputerNerd', 'MikE', 'jspro']

for username in new_usernames:
    if username.lower() in current_usernames:
        print(f"Sorry, {username} has already been taken. Choose another one!")
```
- `else` code block runs when `if` condition is `False`

`==` is used when we want to check for equality and `!=` is use when we want to check for inequality.
```python
dinner = "soup"

if dinner != "pizza":
    print("Hold on! Change the dinner!")
```

### `and`, `in` and `not in`
Some times we want to check two or more conditions at the same time in order for a code block to run. `and` helps us to define several conditions in an `if` statement. If one of these conditions is `False`, Python interpreter will skip the code block. All of the conditions should be `True` in order for the Python interpreter to run the code block.
```python
number = 65

if (number < 80) and (number > 60):
    print("The number is in the zone")
```
To check if there is a value present in a list, we can use `in` in the `if` condition to see if a specific value is present inside a list.
```python
names = ['johnny', 'ann', 'ted', 'peter']

if 'ann' in names:
    print("Ann is enjoying the party!")
```
Likewise, we can use `not in` to see if a value is **not** present in a list.
```python
names = ['johnny', 'ann', 'ted', 'peter']

if 'larry' not in names:
    print("Unfortunately, Larry couldn't make to the party")
```

### `if-esle` statements
Most of the conditional codes have an additional code block that runs if the `if` condition is `False`. `else` code block only runs when `if` fails and we do not want to check for specific a condition.<br>
Here is the example from the earlier part + `else` code block to run if the username provided is unique.
```python
current_usernames = ['mike', 'ninjaprogrammer', 'johnny', 'pythonpro', 'computernerd']

new_usernames = ['john', 'ComputerNerd', 'MikE', 'jspro']

for username in new_usernames:
    if username.lower() in current_usernames:
        print(f"Sorry, {username} has already been taken. Choose another one!")
    else: # Additional `else` part
        print(f"Congrats on your new username! {username.upper()}")
```

### `if-elif-else` chain
`if-elif-else` chains are used when we want to check for multiple conditions and run a different block of code for each condition.<br>
Note that `elif` condition runs when the `if` condition fails.
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")
```
You can omit `else` and just use `if-elif` conditions.

### `if` And `if-elif` chain differences
The use of `if` and `if-elif` chains really depends on what you want your program to do.<br>
`if` chains are used when you want to check every condition without the Python interpreter skipping them, as it does in `if-elif` chains. If the first `if` condition is `True` in an `if-elif` chain, the Python interpreter skips the `elif` condition and runs the `if` code. However, if you use `if` chains, the Python interpreter will not skip any condition; it will run the code if the condition results in `True`.
<br>
`if` chain example:

```python
names = ['alice', 'ted', 'rose', 'parker']

if 'alice' in names:
    print("Welcome, Alice!")
if 'parker' in names:
    print("Welcome, Parker!")
if 'mike' in names:
    print("Welcom, Mike")
```

### Checking A List's Status
We can check whether a list is empty or not by just writting the list's name after the `if` statement.
```python
names = []

if names:
    print("Hello everybody.")
else:
    print("Why no body is here?")
```

### Using Multiple Lists
```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}!")

print("\nFinished making your pizza!")
```