my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

# now both lists are the samne but two seperate lists.
print(friends_foods)
print(my_foods)

my_foods.append('cheesburger')
friends_foods.append('hot dog')
# now we can see that the lists are seperate and can be used indpendantly
print(friends_foods)
print(my_foods)

# you need to specify a slice to make two seperate lists
# this doesn't work as now both titles link to the same list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods

my_foods.append('hamburger')
# I have only added hamburger to my_foods but friends foods is the same list
# it will show the same list as my_foods without the [:] indexing for the slice
# which allows up to pull that slice (can be the full list) into a new list.
print(friends_foods)

# below u

friends_foods = my_foods[:]

for food in my_foods:
    print(food)

for food in friends_foods:
    print(food)
