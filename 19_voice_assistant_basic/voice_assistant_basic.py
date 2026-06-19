import datetime

COMMANDS = ["time", "date", "help", "quit"]


def answer(command):
    command = command.strip().lower()

    if command == "time":
        return datetime.datetime.now().strftime("It is %H:%M.")

    if command == "date":
        return datetime.datetime.now().strftime("Today is %d/%m/%Y.")

    if command == "help":
        return "Available commands: " + ", ".join(COMMANDS)

    if command == "quit":
        return "quit"

    return "I do not know this command yet. Type help to see the list."


print("Small local assistant. Type help to start.")

while True:
    user_command = input("> ")
    reply = answer(user_command)

    if reply == "quit":
        print("Goodbye.")
        break

    print(reply)
