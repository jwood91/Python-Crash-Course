# Start with users that ne"ed to be verified.
# and an empty list to hold confirmed users
unverified_users = ["james", "june", "john", "jules"]

confirmed_users = []

# Verify unconfirmed users until there are none left

while unverified_users:
    current_user = unverified_users.pop()

    print("Verifying user:  " + current_user.title())
    confirmed_users.append(current_user)
# Display confirmed users
print("\nThe following users have been confirmed ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
