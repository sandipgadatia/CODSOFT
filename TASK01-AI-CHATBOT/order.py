import json

class OrderHandler:
    def __init__(self):
        with open("data/menu.json", "r") as f:
            self.menu = json.load(f)
        self.current_order = {}
        self.order_confirmed = False

    def handle_order(self, entities):
        pizza_type = entities.get("pizza_type")
        size = entities.get("size")
        if not pizza_type or pizza_type not in self.menu:
            return "Sorry, we don't have that pizza type. Please choose from our menu."

        if not size:
            return "Please specify a size for your pizza (small, medium, large)."

        self.current_order = {"pizza_type": pizza_type, "size": size}
        return f"Great! You've ordered a {size} {pizza_type} pizza. Would you like dine-in or take-out?"

    def get_menu(self):
        menu_str = ""
        for pizza, sizes in self.menu.items():
            menu_str += f"{pizza.capitalize()} - Sizes: "
            menu_str += ", ".join([f"{size.capitalize()} (${price})" for size, price in sizes.items()])
            menu_str += "\n"
        return menu_str

    def confirm_order(self, entities):
        mode = entities.get("mode")
        if not self.current_order:
            return "You don't have any order to confirm."
        
        if not mode:
            return "Please specify if you want dine-in or take-out."

        self.current_order["mode"] = mode
        self.order_confirmed = True
        return f"Your order for a {self.current_order['size']} {self.current_order['pizza_type']} pizza is confirmed for {mode}. Thank you!"

    def provide_bill(self):
        if not self.order_confirmed:
            return "You don't have any confirmed order."

        pizza_type = self.current_order["pizza_type"]
        size = self.current_order["size"]
        price = self.menu[pizza_type][size]
        return f"Your total bill is ${price}. Thank you for ordering with us!"

