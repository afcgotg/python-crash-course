# 8-9 Messages

def show_messages(messages):
	for message in messages:
		print(message)

messages = ["Hey, how are you?", "What time is it?", "It's raining rightn now?"]
show_messages(messages)

# 8-10 Sending Messages

sent_messages = []
def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

# 8-11 Archived Messages

messages = ["Hey, how are you?", "What time is it?", "It's raining rightn now?"]
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)