# Working with Lists and Tuples

### `for` Loop
We can use `for` loops to go through each item of a list and do same operation on them.<br>
We use indentation to create several blocks of code. Indentation is the space and the blocks we put to the code to have several sections working with each other.
```python
names = ['alice', 'mike', 'bob']

for name in names:
    print(f"Me and {name.title()} are friends!")
print(f"I like all of my friends.") # This line is not in the `for` loop because it's not indented
```
### Making Numerical Lists
`range()` function: `range()` creates numbers according to the given range.<br>
If we write `range(1, 11)`, the function will give the numbers from 1 to 10. `range()` function has off-by-one behavior in the second value (ending range).<br>
`range()` has a third value which is step (it's set to 1 by default).
```python
for number in range(1, 11):
    print(number)
```
```python
squares = []

for value in range(1, 11):
    squares.append(value ** 2) # Changing and adding value to the list
print(squares)
```
### Simple Statistics with a List of Numbers
We can use some of the mathematical functions in python to find minimum, maximum and sum of a set of numbers.
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(numbers)) # Prints the smallest number in the list
print(max(numbers)) # Prints the largest number in the list
print(sum(numbers)) # Prints the sum result of all numbers in the list
```
### List Comprehensions
List comprehensions are used in advanced programming levels. They are an easy way to specify and append values to a list that is written within the list.

```python
squares = [value ** 2 for value in range(1, 11)]
```
There is no colon needed in these types of `for` loops which are inside the list.

### Working With Parts Of a List
We can work with different parts of a list with a method named "slicing". Slicing helps us to define a starting and ending index in which we can work with it later (ending index is off-by-one).<br>
Slicing also accepts a third value which defines the steps in the given range (it's set to 1 by default). 
```python
names = ['alice', 'mike', 'bob', 'larry', 'david', 'jack']

print(names[0:2]) # Prints the first two names
print(names[2:4]) # Prints the two middle names
print(names[-2:]) # Prints the last two names
print(names[0:5:2]) # Two steps jump in the defined range
```
In the slicing there is only one value required at minimum. Meaning that you can either define starting or ending value and python interpreter will figure out the rest.<br>
If you only define the starting index, python interpreter will continue till the end of the list no matter the length.
```python
names = ['alice', 'mike', 'bob', 'larry', 'david', 'jack']

print(names[2:]) # It will select from 'bob' to the end of the list
```
If you only define the ending index, python interpreter will start from 0 index and continue till the defined ending index (remember that ending index is off-by-one!)
```python
names = ['alice', 'mike', 'bob', 'larry', 'david', 'jack']

print(names[:4]) # It will start selecting from 'alice' to 'larry'
```

### Additional
`for` loop in slices:
```python
names = ['alice', 'mike', 'bob', 'larry', 'david', 'jack']

for name in names[:5]:
    print(name.title())
```

We can copy/duplicate a list as a separate list with slicing.

```python
my_favorites = ['pizza', 'chocolate cake', 'sundae ice cream']

# This line will make a complete copy of the 'my_favorites' list to the 'menu'
menu = my_favorites[:]
menu.append('gummy bears') # This item will only be added to the 'menu' list.
```
---
<br>

# Tuples
Tuples are just like the lists, but they are immutable. Meaning that once the data is written, you cannot change it later.<br>
You can work with tuples just like the lists but new data cannot be assigned to them.
```python
names = ('alis', 'ted', 'ann', 'sophia')

print(names[1:3]) # Slicing works in tuples too!

for name in names[1:]:
    print(name)
```
Although we cannot change the values inside a tuple, but we can redefine and over write them.
```python
names = ('alis', 'ted', 'ann', 'sophia')

names = ('johnny', 'sara', 'peter', 'mark') # Changing the values of a tuple by redefining
```