# Dictionaries

### How To Create A Dictionary?
The indicators of dictionaries in Python is `{}`. Dictionaries have two parts, key and value.
```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```
When we select a key from a dictionary, Python interpreter returns the value of the key.

### Adding New Key-Value Pairs
We can add new key-value pairs first by writing the dictionary's name then writing the new key name in the brackets and write the value after the equal `=` sign.
```python 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

### Modifying Values in a Dictionary
For modifying an existing value of a key, the method is identical to adding new key-value pairs, but this time the value is changed.
```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien['color']}")
```
Following is a combination of dictionary modification and an `if-elif-else` chain.
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
```

### Removing Key-Value Pairs
We can delete a key-value pair with `del`. All `del` needs is the name of the dictionary and the key we want to delete the key-value of.
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)
```
Note that deleted key-value pairs with `del` are permanently removed.

### Using `get()` to Access Values
When we select a value that doesn't exist using brackets, the Python interpreter results in a traceback, showing a `KeyError` which stops the program from running. We can fix this by fetching values with the `get()` method. The `get()` method takes two arguments: the name of the key and the value to return if the specified key doesn't exist.
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)
```
If the key exists, you will get the corresponding value associted with the key using `get()` method.

### Looping Through a Dictionary
When we want to use `for` loop for dictionaries we should write two temporary variables for the `for` loop as a dictionary item contains a key and a value.<br>
`item()` returns a sequence of key-value pairs.
```python
user_0 = {
    'username': 'johnsm',
    'first': 'john',
    'last': 'smith',
}

for key, value in user_0.item():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```
An other example:
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


for name, language in favorite_languages.items():
print(f"{name.title()}'s favorite language is {language.title()}.")
```

### Looping Through All the Keys in a Dictionary
Use `keys()` method to extract only the keys and loop through them with `for` loop.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys(): # Looping keys only!
    print(name.title())
```
Note that when looping though a dictionary Python loops through the keys by default without putting `keys()` method. But for the sake of clarity it is a good practice to put `keys()` method in the `for` loop.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages: # Keys are only selected by default
    print(name.title())
```

### Looping Through a Dictionary’s Keys in a Particular Order
To print a dictionary in order, use `sorted()` method to make an ordered copy of the dictionary.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
print(f"{name.title()}, thank you for taking the poll.")
```
This code will print the keys in particular order (in this case in alphabetical order)

### Looping Through All Values in a Dictionary
Use `values()` method when you only want to select values in a dictionary.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
print(language.title())
```
In this code we have a repetitive value which is "python". In small lists it's okay, but in larger lists (let's say millions of values in a list!) it would be a problem to handle them. We can eliminate repetitive lists with `set()` method.<br>
A `set` is a collection in which each item must be unique.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
print(language.title())
```
`set()` identifies unique items in the collection and builds a set from those items, resulting in nonrepetitive lists.

### Nesting
Sometimes we want to create a list of dictionaries as value or lists inside a dictionary. This is called nesting.

### A List of Dictionaries
We can manage several similar related dictionaries in a list and use them more efficiently.
```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```
To make it more realistic we can create dictionaries automatically and add them all into a list.
```python
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
```

### A List in a Dictionary
It is sometimes a good idea to put lists inside a dictionary. For example if you want to store more than one value in a key inside of a dictionary.
```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize of the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
```

### A Dictionary in a Dictionary
You can nest a dictionary inside another dictionary. The following example shows the code for storing users of a website and using their usernames as keys in order to store the other information related to specific user.
```python
users = {
    'johnsmith': {
        'first': 'johnny',
        'last': 'smith',
        'location': 'new york',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```