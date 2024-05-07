from model_node import Node

class Story():
    def __init__(self, title, start_id, start_option_title, start_description, fuel_supply, oxygen_supply, food_supply):
        # initializes a Story object with its properties

        self.title = title # the title of your story
        self.current_node = Node(start_id, start_option_title, start_description, fuel_supply, oxygen_supply, food_supply) #the current Node of your story
        self.first_node = self.current_node # the first Node of your story
        self.fuel_supply = 20
        self.oxygen_supply = 20
        self.food_supply = 20

    def add_new_child(self, parent_id, child_id, child_option_title, child_description, fuel, oxygen, food):
        # adds a new child node to a parent node

        parent_node = self.first_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description,
            fuel_supply = fuel,
            oxygen_supply = oxygen,
            food_supply = food
        )
        
        parent_node.add_child(new_child_node)

    def connect_existing_child(self, parent_id, existing_child_id):
        # connects an existing child node to a parent node
        parent_node = self.current_node.find(parent_id)

        existing_node = self.current_node.find(existing_child_id)

        parent_node.add_child(existing_node)

    def get_current_children(self):
        # returns a list of the children of the current node

        return self.current_node.children

    def set_current_node(self,chosen_node):
        # sets the current node to the chosen node

        self.current_node = chosen_node
  
    def is_finished(self):
        # returns True or False based on if the current node has children
        if len(self.current_node.children) == 0:
            return True
        elif self.fuel_supply < 0:
            return True
        elif self.oxygen_supply < 0:
            return True
        elif self.food_supply < 0:
            return True
        else:
            return False 

    def add_fuel_supply(self, add_fuel):
        # changes the fuel supply based on the nodes
        self.fuel_supply = self.fuel_supply + add_fuel

    def add_oxygen_supply(self, add_oxygen):
        # changes the oxygen supply based on the nodes
        self.oxygen_supply = self.oxygen_supply + add_oxygen

    def add_food_supply(self, add_food):
        # changes the food supply based on the nodes
        self.food_supply = self.food_supply + add_food

    def reset_supplies(self):
        # resets supplies back to 20
        self.fuel_supply = 20
        self.oxygen_supply = 20
        self.food_supply = 20