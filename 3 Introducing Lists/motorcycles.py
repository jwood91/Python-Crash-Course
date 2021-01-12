# You can change the values of items within the list:
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# This will replace the first item
motorcycles[0] = 'ducati'

# To add items to a list you need to use the .append() function
motorcycles.append("ducati")
print(motorcycles)

# You can use the append function to build lists dynamically. so you can start
# with an empty list and add items.
motorcycles = []
print(motorcycles)
motorcycles.append("honda")
print(motorcycles)

# You can insert an item at any point in the list by using the .insert()
# fuction.  index position first then second the item to add example below:
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(1, "ducati")
print(motorcycles)

# You can use a del statement to remove an item from anywhere in the list
# if you know the index location in the example below you will no longer be
# able to access the item once the del statement is run
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[0]
print(motorcycles)


# you can remove items from the list using the .pop() method. This lets you
# remove an item from a list but then continue working with it.
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.pop()
print(motorcycles)
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()
motorcycles.append(popped_motorcycle)
print(motorcycles)

# you can also pop an item from any indexed position
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print(motorcycles)
motorcycles.append(first_owned)
print(motorcycles)

# When deciding to use a del statement or pop() method think do I need to use
# that item again.  If you don'tneed it you can use the del statement, if you
# want to use it then use the pop() method.

# Sometimes you want to remove an item you do not know the index of you can use
# the .remove() method.
motorcycles = ["honda", "suzuki", "ducati", "yamaha"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

# Similar to the pop() method you can work with the item from the remove()
# method.
motorcycles = ["honda", "suzuki", "ducati", "yamaha"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive + " is too expensive for me.")
