usernames = ['iyan', 'naufal', 'akbar', 'fayaz', 'ndaru']

for username in usernames:
    if username == 'akbar':
        print("Hello akbar, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")