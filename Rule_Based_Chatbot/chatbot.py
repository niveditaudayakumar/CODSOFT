# Improved Rule-Based Chatbot with Keyword Detection

print("Chatbot: Hello! I am your AI chatbot.")
print("Chatbot: Ask me something. Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Chatbot: Hello! How can I help you?")

    # Name question
    elif "name" in user_input:
        print("Chatbot: My name is RuleBot, your simple AI chatbot.")

    # AI question
    elif "ai" in user_input:
        print("Chatbot: AI stands for Artificial Intelligence. It allows machines to perform tasks that normally require human intelligence.")

    # How are you
    elif "how are you" in user_input:
        print("Chatbot: I am functioning properly. Thanks for asking!")

    # Capabilities
    elif "what can you do" in user_input or "help" in user_input:
        print("Chatbot: I can answer simple questions, greet you, and tell jokes.")

    # Joke
    elif "joke" in user_input:
        print("Chatbot: Why was the computer cold? Because it forgot to close its Windows!")

    # Creator question
    elif "who created you" in user_input or "creator" in user_input:
        print("Chatbot: I was created using Python for an AI internship task.")

    # Exit
    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    # Unknown input
    else:
        print("Chatbot: Sorry, I don't understand that yet.")
