import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"],
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you built")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
