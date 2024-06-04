from order import OrderHandler
from nlp import NLPProcessor

class Chatbot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.order_handler = OrderHandler()

    def get_response(self, user_input):
        intent, entities = self.nlp_processor.process(user_input)

        if intent == "greeting":
            return "Hello! Welcome to our pizza restaurant. How can I assist you today?"
        elif intent == "order_pizza":
            if not entities.get("pizza_type"):
                return "Sure, here's our menu: \n" + self.order_handler.get_menu() + "\nWhich type of pizza would you like?"
            return self.order_handler.handle_order(entities)
        elif intent == "show_menu":
            return "Here's our menu: \n" + self.order_handler.get_menu()
        elif intent == "assist_order":
            return "What would you like to order? Please specify the type and size of the pizza."
        elif intent == "confirm_order":
            return self.order_handler.confirm_order(entities)
        elif intent == "provide_bill":
            return self.order_handler.provide_bill()
        elif intent == "farewell":
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

