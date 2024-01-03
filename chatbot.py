import re

def simple_chatbot(user_input):
    user_input = user_input.lower()
    rules = {
        r'\b(hi|hello|hey)\b': 'Hello! How can I help you?',
        r'\b(how are you)\b': 'I am just a computer program, but thanks for asking!',
        r'\b(what is your name)\b': 'I am a simple chatbot.',
        r'\b(bye|goodbye)\b': 'Goodbye! Have a great day.',
        r'\b(thank you|thanks)\b': 'You\'re welcome!',
        r'\b(who are you)\b': 'I am a chatbot designed to assist with basic queries.',
        r'\b(what can you do)\b': 'I can provide information, answer questions, and have simple conversations.',
        r'\b(time)\b': 'I don\'t have the capability to provide real-time information like the current time.',
        r'\b(joke)\b': 'Why don\'t scientists trust atoms? Because they make up everything!',
        r'\b(weather)\b': 'I don\'t have access to real-time weather information.',
        r'\b(i love you)\b': 'I don\'t have access to your personal information.',

    }
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)