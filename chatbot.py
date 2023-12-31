def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define some predefined rules and responses
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    questions = ["how are you", "what's up", "how's it going"]
    identification =["who are you","introduce yourself","may I know your name"]
    default_response = "I'm sorry, I don't understand that."


    # Check user input against predefined rules
    if user_input in greetings:
        return "Hello! How can I help you today?"
    elif user_input in farewells:
        return "Goodbye! Have a great day!"
    elif any(q in user_input for q in questions):
        return "I'm doing well, thank you for asking."
    elif any(i in user_input for i in identification):
        #user_input in identification:
        return "I am chatbot-a computer program for automatic interaction!!"
    else:
        return default_response

# Simple loop to keep the chatbot running
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if the user types "exit"
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Get and print the chatbot's response
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
