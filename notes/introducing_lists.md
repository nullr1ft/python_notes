# Lists

### Index In Lists
From right, lists start from 0 and continue.<br>
From left, lists start from -1 and continue.
```python
#           0        1        2        3        4
names = ['john' , 'jimmy', 'bob', 'peter', 'alice']
#          -5       -4       -3        -2      -1

print(f"Hello there! {names[0].title()} welcome to the party!")
print(f"Hello there! {names[-2].title()} welcome to the party!")
```

### Adding To The List & Modifying
There are several ways to add data to a list.<br><br>
First, adding data without any index number which will add the data to the end of the list:
```python
names.append('mary')
```
Second, adding data with index number which will add the data to the specified place:
```python
names.insert(-1, 'sam')
```
We can also modify any data we want inside the list:
```python
name[1] = 'andrew'
```

### Organizing Lists
We can either sort lists permanently or temporary<br>

Permanent:
```python
names.sort() # will sort the list alphabetically (A - Z)
names.sort(reverse=True) # will sort the list alphabetically reverse (Z - A)
names.reverse() # reversing in original order (it's simply reversing)
```

Temporary:
```python
print(sorted(names)) # will temporarily sort the list alphabetically (A - Z)
print(sorted(names, reverse=True)) # will temporarily sort the list alphabetically reverse (Z - A)

```

We can find the length of a list with the help of `len()`:
```python
print(len(names))
```

### Removing From The List
We actually have 3 ways to delete an item from a list.

`del`:<br>
This is used when we want to delete something permanently and we don't intend to use it later.
```python
del names[3]
```

`pop()`:<br>
If we want to both delete something and intend to use it later, we can use `pop()`.
```python
removed_person = names.pop(0)
```

`remove()`:<br>
Sometimes we don't know the index number of the item we want to remove! That's when we use the `remove()`. (we can also use the removed item later like `pop()` like shown in the example)
```python
removed_person = 'jimmy'
names.removed(removed_person)
```