  

class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
  #Returns the value of the coffe(key) given. 
  def get_price(self, item):
    if item not in self.menu:
        raise ValueError(f"{item} is not available on the menu.")
    return self.menu[item]
  #Adds an item to the menu.
  def add_item(self, item, value):
    self.menu[item] = value
