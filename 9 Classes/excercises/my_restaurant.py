from restaurant import Restaurant

my_restaurant = Restaurant('Pizza Express', 'Italian')
your_restaurant = Restaurant('Noodle Bar', 'thai')
their_restaurant = Restaurant('turtle bay', 'carribbean')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
their_restaurant.describe_restaurant()

my_restaurant.open_restaurant()
your_restaurant.open_restaurant()
their_restaurant.open_restaurant()

my_restaurant.update_number_served(30)

my_restaurant.read_number_served()
