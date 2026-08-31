# ---------- A basic conditional code ----------
cars = ['audi', 'BMW', 'subaru', 'toyota']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# If you want to test a value of a variable, lower case that and test it with (==) (because equality in python case sensitive)
name = 'John'
name.lower() == 'john' # This will return the 'True' statement

dinner = 'soup'
if dinner != 'pizza': # To check Inequality we can use '!=' to create an if statement
    print("Hold on! Dinner is not good for tonight.")

# ---------- and or in not ----------
number = 56
if (number < 60) or (number > 60): # In 'or' when both or one condition is True it returns True
    print('True')                  # When both of the conditions are False 'or' returns False 
# In 'and' if two conditions are True it will return 'True' but if one or two of the condions is False it will reture 'False'
if (number == 56) and (number > 10): # You can use parentheses for readability, but they are not required
    print('True')

# To see whether a particular value is in the list we use keyword'in'
names = ['johnny', 'ann', 'ted', 'peter']

if 'ann' in names: # Checks if 'ann' is in the 'names' list
    print("Yes, she/he is in the invite list!")
if 'jack' not in names: # 'not' is checking whether a particular value is -not- in the 'names' list
    print("No, she/he is not in the invite list!")

# ---------- if-else Statements ----------
# In simple 'if-else' statements like this one of the one of the two actions will always be excuted
age = 29
if age >= 18: # 'if' statement is the first condition to be reviewed. if True 'else' statement will not be run
    print("You are old enough to vote!")
else: # 'else' is the second statement runs if the 'if' statement is False
    print("Sorry, you are too young to vote.")

# ---------- if-elif-else Chain ----------
# In if-elif-else chain code block will run like a chain meaning in case one fails the other one will run instead
# In case one of the conditions beceome True Python will ignore the rest and will fun the that condition operation
# Note that you can write as many as 'elif' conditions as you want after the 'if' condition
# 'else' is not really require to put in if-elif chain
age = 12
if age < 4: # This will check if the person is under 4 years old
    price = 0
elif age < 18: # 'elif' is really an other 'if' test which runs only if the previous test failded
    price = 25
else: # Python will run 'else' if the 'elif' condition is fails
    price = 40
print(f"Your admission cost is ${price}")

# ---------- if and if-elif chain difference ----------
# If we need to check -all- the conditions no matter what we should use multiple 'if' statements
# If we need to just check if a certain conditions is True and then run an operation based on that we can use 'if-elif' chain
# Overall if you want just one block of code to run use 'if-elif-else' chain
# If more than one block of code needs to be run you should use series of independent 'if' statements
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: # In this case we want to check all of these conditions without skipping
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

# ---------- Checking That a List Is Not Empty ----------
# When the name of a list is used in an 'if' statement Python returns True if the list contains at least one item
# An empty list evaluates to False
requested_toppings = []

if requested_toppings: # This 'if' statement checks if the list have any value in it
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping} ...")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# ---------- Using Multiple Lists ----------
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}!")

print("\nFinished making your pizza!")

# ---------- Checking Username Availability ----------
# Checking both uppercase of lowercase usernames for availability
current_users = ['spy', 'admin', 'hitman', 'cyberpunk', 'hacker']
new_users = ['coder', 'spy', 'HACKER', 'robot', 'computer']
# So here were we lowercase all current users to compare them the new lowercase users
lowercase_users = [user.lower for user in current_users]

for new_user in new_users:
    if new_user.lower() in lowercase_users: # Lowercasing the 'new_user' to see if they are in 'lowercase_users'
        print(f"Sorry, {new_user} is not available. Please choose an other username.")
    else:
        print(f"{new_user} is available to use.")