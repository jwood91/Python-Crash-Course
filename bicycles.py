bicycles = ['trek', 'canodale', 'redline', 'specialized']
print(bicycles[0])
# indexing starts at 0 so 0 is the first item in the list

print(bicycles[0].title())

# Python has a special way of accessing the final item in the list with -1
print(bicycles[-1].title())

print("my first bicycle was a " + bicycles[3].title() + ".")
