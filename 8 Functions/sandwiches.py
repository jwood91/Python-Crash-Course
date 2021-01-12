def user_sandwich(*fillings):
    """summarizes what's in the sandwich"""
    print("\nThis sandwich contains: ")
    for filling in fillings:
        print("- " + filling)


user_sandwich("prawns", "mayonaise", "lettuce", "cucumber")
user_sandwich("tuna", "cucumber", "ketchup")
user_sandwich("ham", "cheese", "tomato")
