current_users = ['abi', 'iyan', 'akbar', 'al', 'naufal']
new_users = ['akbar', 'rohmad', 'nurhuda', 'al', 'asih']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' has already been used. You will need to enter a new username.")
    else:
        print(f"Great, the username '{new_user}' is available.")