# ----------'for' loop ----------
# to do same operation on every list item we can use 'for' loop to do it
magicians = ['alice', 'david', 'carolina']

for magician in magicians: # 'magician' here is a temporary variable 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!") # This is not part of the 'for loop' because it is not in indentation
# indentation is the space and the blocks we put to the code to have several sections working with each other

# ---------- Making Numerical Lists ----------
# 'range()' function
for numbers in range(1, 6): # we have off-by-one behavior in 'range()'
    print(numbers)          # if you pass one value to range like this 'range(6)' it will start from 0

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# ---------- Simple Statistics with a List of Numbers ----------
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits)) # will show the maximum number in the list
print(min(numbers)) # will show the minimum number in the list
print(sum(numbers)) # will add the all the numbers and show the result

# ---------- List Comprehensions ----------
# there is an other way to specify and append value to a list with in the list
sqrares = [value ** 2 for value in range(1, 11)] # there is no colon used in this types of 'for' loop
print(sqrares)

# ---------- Working With Parts Of a List ----------
# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # the first value is where to start and the second one is where to end which is off-by-one
print(players[0:3:2]) # if the third value added, it specifies how many items should python skip between items
print(players[:3]) # if the first value (the beginning) is not added, python will begins from 0 index in the list
print(players[1:]) # if the second value (the ending) is not added, python continue till the end of the list

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'chocolate cake', 'sundae ice cream']
friend_foods = my_foods[:] # this will make a complete copy of the 'my_foods' list to the 'friend_foods'