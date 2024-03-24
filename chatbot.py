import random
from nltk.chat.util import Chat, reflections
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks! How about you?']],
    ['(.*) your name?', ['My name is ChatBot.']],
    ['(.*) help (.*)', ['Sure, I can help you. What do you need assistance with?']],
    ['(.*) your age?', ['I am a computer program. I don\'t have an age.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
    ['what is your purpose?', ['I am here to assist you with any questions or tasks you may have.']],
    ['tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'I’m reading a book on anti-gravity. It’s impossible to put down!']],
    ['how can I contact support?', ['You can contact support by emailing support@example.com or calling our hotline at 1-800-123-4567.']],
    ['what is the meaning of life?', ['The meaning of life is subjective and can vary from person to person.']],
    ['thank you', ['You\'re welcome!', 'No problem.', 'Anytime!']],
    ['sorry|apologies', ['No need to apologize.', 'It\'s okay.', 'No worries.']],
    ['what are your hobbies?', ['I enjoy chatting with users like you!', 'I like learning new things and helping people.']],
    ['what is your favorite color?', ['I don\'t have eyes, so I don\'t have a favorite color.']],
    ['how do I reset my password?', ['You can reset your password by visiting our website and clicking on the "Forgot Password" link.']],
    ['where are you from?', ['I am a chatbot, so I don\'t have a physical location.']],
    ['do you have any siblings?', ['No, I am the only chatbot here.']],
    ['what do you like to eat?', ['I don\'t eat anything, as I am not a living being.']],
    ['what languages do you speak?', ['I can understand and communicate in English.']],
    ['can you tell me about yourself?', ['I am a chatbot designed to assist users with their inquiries.']],
    ['what is the weather like today?', ['I don\'t have access to real-time data. You can check the weather on a weather website.']],
    ['what time is it?', ['I don\'t have access to the current time.']],
]
chatbot = Chat(pairs, reflections)

def chat():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
if __name__ == "__main__":
    chat()
