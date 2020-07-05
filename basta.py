#ALL OF THE MENUS
#BRUNCH MENU
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#EARLY BIRD MENU
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

#DINNER MENU
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

#KIDS MENU
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#AREPA MENU
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# ----------------------- #

#MENU CLASS
class Menu():
  def __init__(self, name, items, start_time, end_time): 
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self): #prints out a string that gives the name of the menu and when its available
    menu_text = "This is the {menu} menu and it's available from {start} to {finish}."
    return menu_text.format(menu=self.name, start = self.start_time, finish = self.end_time)

  def calculate_bill(self, purchased_items): #finds total bill
    self.purchased_items = purchased_items
    total = 0
    for item in purchased_items:
      for food, price in self.items.items(): #goes through key and value in the dictionary of menu items
        if item == food: #if an item is the same as an item in the dictionary, add the price of that to the total
          total += price
        else: #if item isnot there, skip it
          continue
    return total


#FIVE MENUS
brunch = Menu("Brunch", brunch_items, 11, 16)
#print(brunch.end_time) #tests brunch menu

early_bird = Menu("Early Bird", early_bird_items, 15, 18)
#print(early_bird.items) #tests early bird menu

dinner = Menu("Dinner", dinner_items, 17, 23)
#print(dinner.name) #tests dinner

kids = Menu("Kids", kids_items, 11, 21)
#print(kids.items) #tests kids menu

arepas = Menu("Take a' Arepa", arepas_items, 10, 20)
#print(arepas.name)

#print(kids) #tests the string that says the name and availability of menu

#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"])) #tests calculate_bill method on brunch
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])) #tests calculate_bill method on early bird purchase

# ----------------------- #

#FRANCHISE CLASS
class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self): #tells the address of the store
    address_string = "This franchise is located at {address}"
    return address_string.format(address = self.address)

  def available_menus(self,time):
    self.time = time
    available_items = []
    for options in self.menus:
      if options.start_time <= time and options.end_time >= time:
        available_items.append(options.items)
    return available_items 

all_menus = [brunch, early_bird, dinner, kids]

#THREE FRANCHISES
flagship_store = Franchise("1232 West End Road", all_menus)
#print(flagship_store.menus)

new_installment = Franchise("12 East Mulberry Street", all_menus)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas)
#print(arepas_place.address)

#print(new_installment) #tests string printing method

#print(flagship_store.available_menus(12)) #test 1
#print(flagship_store.available_menus(17)) #test 2

# ----------------------- #

#BUSINESS CLASS
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#TWO BUSINESSES
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
#print(basta.franchises)
take_a_arepa = Business("Take a' Arepa", arepas_place)
#print(take_a_arepa.franchises.menus)


