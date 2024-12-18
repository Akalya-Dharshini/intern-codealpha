import nltk # type: ignore
from nltk.chat.util import Chat, reflections # type: ignore

# Define pairs of user inputs and corresponding bot responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hey there! How can I assist you?']),
    (r'how are you?', ['I am good, thank you! How about you?', 'I am doing well, thanks for asking!']),
    (r'what is your name?', ['I am a chatbot created to assist you. What can I do for you today?']),
    (r'quit', ['Goodbye! Have a great day!']),
    (r'(.*)', ['Sorry, I didn\'t understand that. Can you ask something else?'])
]

# Create a chatbot using the pairs and reflections (for changing pronouns like "I" to "you")
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def start_chat():
    print("Chatbot: Hi! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the chatbot
start_chat()
