
# Practical 7: Rule-Based Chatbot

import re
from datetime import datetime

# Predefined rules
rules = [
    (r"hi|hello|hey", "Hello! How can I help you?"),
    (r"how are you", "I am fine, thank you!"),
    (r"your name|who are you", "I am PyBot, a rule-based chatbot."),
    (r"what is ai", "AI stands for Artificial Intelligence."),
    (r"help", "I can answer basic questions about AI."),
    (r"thanks|thank you", "You are welcome!")
]


def get_reply(message):
    message = message.lower().strip()

    # Name recognition
    match = re.search(r"my name is (\w+)", message)
    if match:
        return "Nice to meet you, " + match.group(1).capitalize()

    # Time response
    if re.search(r"\btime\b", message):
        return datetime.now().strftime("Current time: %H:%M")

    # Match predefined rules
    for pattern, reply in rules:
        if re.search(pattern, message):
            return reply

    return "Sorry, I did not understand."


def main():
    print("Welcome to PyBot!")
    print("Type 'bye' to exit.")

    while True:
        message = input("You: ").strip()

        if message.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye!")
            break

        if message == "":
            print("Bot: Please type something.")
            continue

        print("Bot:", get_reply(message))


if __name__ == "__main__":
    main()
