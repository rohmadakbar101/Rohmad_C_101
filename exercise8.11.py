def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


messages = [
    "Hello, how are you?",
    "Keep learning Python!",
    "Never give up!",
    "Have a great day!"
]

sent_messages = []

send_messages(messages.copy(), sent_messages)

print("nOriginal messages:")
print(messages)

print("Sent messages:")
print(sent_messages)