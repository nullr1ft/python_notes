# ---------- Tuples ----------
names = ('alis', 'ted', 'ann', 'sophia')
# in tuple you can not change the value inside
# you can access it just like a list with indexing and other ways
# tuples are just like a list but instead of [] you replace ()

names = ('johnny', 'sara') # although we said we can not change the values inside a tupe ,but we can over write it in the next line
names = ('harris', 'peter') # you can over write the tuple with redefining the entire tuple

# then we can use the redefining tuple:
for name in names:
    print(name)