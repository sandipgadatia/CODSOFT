import re

class NLPProcessor:
    def __init__(self):
        self.intents = {
            "greeting": ["hello", "hi", "greetings", "hey"],
            "farewell": ["bye", "goodbye", "see you"],
            "order_pizza": ["order", "pizza", "want", "get"],
            "show_menu": ["menu", "show", "see", "list"],
            "assist_order": ["assist", "help", "order"],
            "confirm_order": ["confirm", "order", "dine-in", "take-out", "to go"],
            "provide_bill": ["bill", "price", "total"]
        }

    def process(self, user_input):
        user_input = user_input.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in user_input for keyword in keywords):
                return intent, self.extract_entities(user_input)
        return "unknown", {}

    def extract_entities(self, user_input):
        entities = {}
        pizza_types = ["margherita", "pepperoni", "hawaiian", "veggie"]
        sizes = ["small", "medium", "large"]
        modes = ["dine-in", "take-out", "to go"]

        for pizza_type in pizza_types:
            if pizza_type in user_input:
                entities["pizza_type"] = pizza_type

        for size in sizes:
            if size in user_input:
                entities["size"] = size

        for mode in modes:
            if mode in user_input:
                entities["mode"] = mode

        return entities
