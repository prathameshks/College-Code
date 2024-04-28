class SimpleChatBot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "how are you": "I'm a bot, so I don't have feelings, but I'm here to help you. How can I assist you?",
            "what can you do": "I can provide information and answer questions to the best of my ability.",
            "goodbye": "Goodbye! Have a great day!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I didn't understand that. Could you please rephrase?"

chatbot = SimpleChatBot()
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print("Bot: ", response)
