import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hola"],
    "how are you?": ["I'm good, thanks for asking!", "I'm doing fine, how about you?", "I'm doing great. thank you! how about you"],
    "bye": ["Goodbye!", "See you later!", "Bye! have a nice day"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()  

    
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm not sure how to respond to that."


print("Chatbot: Hi! Hope you are doing good.  I'm a simple chatbot. You can ask your doubts else we can have a quick chit-chat. Type 'bye' to exit.")
while True:
    user_message = input("You: ")
    if user_message.lower() == 'bye':
        print("Chatbot: Goodbye! Have a good day!")
        break
    else:
        bot_response = chatbot_response(user_message)
        print("Chatbot:", bot_response)
