class Restaurant():
    """Simple model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes restaurant name and cuisine type attributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints restaurant information"""
        print("\nThe restaurant is called: " + self.name.title())
        print("The type of cuisine is: " + self.cuisine.title())

    def open_restaurant(self):
        """Tells that the restaurant is open"""
        print("\n" + self.name.title() + " is now open for business.")

    def read_number_served(self):
        """shows number of people served"""
        print(
            "There have been " + str(self.number_served)
            + " people served this evening"
        )

    def update_number_served(self, diners):
        """updates number of diners"""
        self.number_served += diners


class IceCreamStand(Restaurant):
    """Simple model of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavour="vanilla"):
        """Initialize traits specific to an ice cream truck"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = flavour

    def flavours(self):
        """show flavours"""
        flavours = ["chocolate", "vanilla", "strawberry"]
        print("We have these flavours: ")
        for flavour in flavours:
            print(flavour.title())

    def flavour_choice(self):
        """prints current flavour choice"""
        print("Your choice is " + self.flavour + " ice cream")
