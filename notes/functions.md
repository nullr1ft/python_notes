# Functions

### What Are Functions?
To simply put, functions help programmers to write a code once and use it everywhere they like without writing it all over again which is more efficient and easier to maintain.

### Defining a Function
A function in Python is defined with `def` keyword. After that, the name of the function comes. After the name, parentheses come which hold the required information for the function to work. If a function doesn't need any information to work with, we should put empty parentheses because they are required in the Python syntax.
```python
def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()
```

### Passing Information to a Function
To use information in a function, we should write appropriate variables in the function definition.
```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username}")

greet_user('john')
```
### The Difference Between Arguments and Parameters
Technically, a parameter is when we define a function and give it a variable (e.g., `greet_user(username)`). Essentially, `username` is the information that the function needs to do its job. This is called a *parameter*.<br>
When we pass a value to a function (e.g., `greet_user('john')`), that value is an *argument*.<br>
Note that you will see sometimes people will use arguments and parameters interchangeably.

### Passing Positional Arguments
When you call a function, Python must match each argument in the function call with appropriate parameters. The simplest way to do this is based on the order of the arguments provided. The values matched up this way are called *positional arguments*.
```python
def describe_pet(animal_type, pet_name):
    """Display simple information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'tom')
```
Order matters in positional arguments and if you put values in the wrong position, you may not get the correct output you expect.

### Passing Keyword Arguments
In keyword-based arguments, you pass name-value pairs to the function. In this way you don't have to worry about the position of the arguments.
```python
def describe_pet(animal_type, pet_name):
    """Display simple information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='ted')
describe_pet(pet_name='ted', animal_type='dog') # Will produce same output as the first one
```
In this way, we specifically tell Python to match parameters with values so Python knows exactly what parameter each argument should be matched with.

### Default Values
We can define some default values in the function definition so that if those arguments are not provided in the function call, Python will use those arguments. Using default values can simplify function calls and clarify the ways that a function can be used.
```python
def describe_pet(pet_name, animal_type='cat'):
    """Display simple information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cookie')
```
In this example, if no `animal_type` is passed to the function, Python will continue with the default value. However, if the `animal_type` argument is passed in the function call (e.g., `describe_pet('jessy', 'fish')`), Python will overwrite the `fish` argument to the default value.<br>
Note that any parameters with default values need to be listed after all the parameters that don’t have default values. This is because Python still treats function calls as positional arguments.

### Returning values
We don't need to always display an output. Instead we can do process on data and return a value or a set of values. We can do this with `return` keyword in Python. We we use `return`, Python sends the output value to the line that called the function.
```python
def formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

person_0 = formatted_name('jerry', 'smith')
print(person_0)
```

### Making an Argument Optional
Sometimes it is a good practice to leave some values optional for the user. In this way people using the function can choose to provide extra information only if they want to.
```python
def formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

person_0 = formatted_name('robbert', 'james')
print(person_0)

person_1 = formatted_name('robbert', 'james', 'john')
print(person_1)
```
Note that Python interprets empty strings as `False` and non-empty strings as `True`.

### Returning a Dictionary
A function can return any type of data you want, including complicated data structures like dictionaries. Instead of returning simple textual information, structured data like dictionaries can be used for a variety of different purposes.
```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of basic information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

person_0 = build_person('jimmy', 'johnson', age=33)
print(person_0)
```

### Passing a List to a Function
Sometimes we find it useful to pass a list to a function in order to work with the items in the list. When you pass a list to a function, the function gets direct access to the content of that list.
```python
def greet_users(names):
    """Print a simple greeting message to the users in the list."""
    for name in names:
        print(f"Hello, {name}!")

usernames = ['john', 'hanna', 'alex']
greet_users(usernames)
```

### Modifying a List in a Function
If you pass a list to a function, you can modify the list inside the body of the function. Every modification made inside the function's body is permanent, enabling you to work efficiently with lists no matter the size of the data inside them.
```python
def making_pizza(available_toppings, added_toppings):
    """Simulate adding each topping on the pizza until nothing is left."""
    while available_toppings:
        current_topping = available_toppings.pop()
        print(f"Adding topping: {current_topping}")
        added_toppings.append(current_topping)

def show_added_toppings(added_toppings):
    """Show all topping that were added to the pizza."""
    print("\nThe following toppings have been added: ")
    for added_topping in added_toppings:
        print(added_topping)

available_toppings = ['mushrooms', 'peppers', 'cheese', 'chicken']
added_toppings = []

making_pizza(available_toppings, added_toppings)
show_added_toppings(added_toppings)
```
While we can write this exact example with `while` loops, writing it with a function makes our code much cleaner and easier to understand, not to mention the efficiency that functions provide, which makes maintaining the code inside them much easier.

### Preventing a Function from Modifying a List
Sometimes you want your list to stay intact, and instead, a copy of your list gets modified in a function. In this way, you can keep the original list and get your desired output from the function while passing an exact copy of the original list.<br>
You can copy a list to a function with the following general format for a function call:
```python
function_name(list_name[:])
```

### Passing an Arbitrary Number of Arguments
Sometimes, you cannot predict how many arguments a function should accept in the future. If this is the case, Python allows a function to collect an arbitrary number of arguments from the calling statement.
```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
The asterisk in the parameter name `*toppings` tells Python to make a tuple called toppings, containing all the values this function receives.

### Using Arbitrary Keyword Arguments
You can accept key-value pairs with double asterisks in function parameters. When you use double asterisks at the beginning of the parameter, Python creates a dictionary, allowing you to pass as many key-value pairs as you like in the calling statement.
```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('john', 'smith',
                             location='paris',
                             field='physics')
print(user_profile)
```

### Storing Function in Modules
We can store our functions in separate files called a *module* and then import that module to our main file.<br>
Them *import* statement tells Python to make that module available in the current file that you are working on.<br>
Modules allow you to use your function in different parts of your program.
```python
# First file (pizza.py)
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```
```python
# Second file (make_pizza.py)
import pizza # Importing pizza as a module

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing Specific Functions
A module may consist of several functions. To import a single function from a module, we should use the following syntax.<br>
Note that you can import as many functions as you want by separating them with comma.
```python
from module_name import function_0, function_1, function_2
```

### Using as to Give a Function an Alias
Sometimes, a function name may conflict with an existing name in your program, or the function name may be too long. In such cases, you can use a short alias or nickname for that function when you import it.
```python
# First file (pizza.py)
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```
```python
# Second file (make_pizza.py)
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```
Here `make_pizza()` function is renamed to `mp()` and imported from *pizza* module.

### Importing All Functions in a Module
By using an asterisk, we can import all functions from a module.
# First file (pizza.py)
```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```
```python
# Second file (make_pizza.py)
from pizza import *

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```