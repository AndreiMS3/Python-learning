
sent_message = "This is a secret message"
unsent_message = "This message has been unsent"

# Write the sent message to the file
with open("message.txt", "w") as file:
    file.write(sent_message)

# Replace the content of the file with the unsent message
with open("message.txt", "w") as file:
    file.write(unsent_message)

# Read the file to verify its content
with open("message.txt", "r") as file:
    content = file.read()
    print(content)  # This should print "This message has been unsent"
    

