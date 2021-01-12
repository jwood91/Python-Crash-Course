from users import Users
from privilages import Admin

this_user = Admin("main", "admin", "0", 2020)
this_user.describe_user()

this_user.privileges.show_privileges()
print("Defining privileges... ")
this_user_privileges = [
    "add user",
    "delete user",
    "add post",
    "delete post",
    "edit post",
]

this_user.privileges.privileges = this_user_privileges
this_user.privileges.show_privileges()
