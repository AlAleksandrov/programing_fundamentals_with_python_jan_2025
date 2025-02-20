class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []
while command != "Stop":
    current_sender, current_receiver, current_content = command.split()
    email = Email(current_sender, current_receiver, current_content)
    emails.append(email)
    command = input()

indices = list(map(int, input().split(', ')))
for index in indices:
    if 0 <= index < len(emails):
        email = emails[index]
        email.send()

for email in emails:
    print(email.get_info())