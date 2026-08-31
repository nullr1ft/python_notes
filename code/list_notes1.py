#           0        1        2        3        4
names = ['john' , 'johnny', 'rick', 'peter', 'dude']
#          -5       -4       -3        -2      -1

# ---------- Messages ----------
print(f"Hello there! {names[0].title()} welcome to the party!")
print(f"Hello there! {names[-2].title()} welcome to the party!")

# ---------- Adding to the list & modifying----------
names.append('rick') # adding without index number which will add to the end of the list
names.insert(-1, 'morty') # adding with specifying the index number
names[1] = 'cool mom' # example of modifying

# ---------- Organizing lists ----------
# "sort()" sorting is permanetly applies to the list
names.sort() # will sort the list from (A - Z)
names.sort(reverse=True) # will sort the list from (Z - A)
names.reverse() # reversing in original order (it is simply reversing)
print(len(names)) # showing the length of a list or anything in general


# "sorted()" sorting is temporarily applies to the list
print(sorted(names)) # will temporarily sort the list from (A - Z)
print(sorted(names, reverse=True)) # will temporarily sort the list from (Z - A)



# ---------- Removing from the list ----------
# "del" in the list is for deleting something permanently and not wanting to use it later
# "pop" in the list is for deleting something and want it to use later like in a variable (locating with indexing numbers)
# "remove" in the list is for deleting something and want it to use like pop we said (lacating with the actual name)


removed_one = 'dude' # using "remove" to delete and also use the deleted item
names.remove(removed_one) # or names.remove('dude')

del names[3]              # using "del" to deleting permanently the list variable

removed_two = names.pop(0) # we are poping out a value in the "names" list and putting it into "remove_two" variable

print(f"Hey there {removed_one.title()} I am so sorry for removing you from the dinner")
print(f"Hey there {removed_two.title()} I am so sorry for removing you from the dinner")
print("John has been removed without any notice!!!!!!!")
print(f"\nThis is the guests that remianed!!: \n{names}")