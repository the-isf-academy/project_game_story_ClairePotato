from model_node import Node

class Story():
    def __init__(self, title, start_id, start_option_title, start_description, fuel_supply, oxygen_supply, food_supply):
        # initializes a Story object with its properties

        self.title = title # the title of your story
        self.current_node = Node(start_id, start_option_title, start_description) #the current Node of your story
        self.first_node = self.current_node # the first Node of your story

    def add_new_child(self, parent_id, child_id, child_option_title, child_description, fuel_supply, oxygen_supply, food_supply):
        # adds a new child node to a parent node

        parent_node = self.first_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description,
            fuel = fuel + fuel_supply,
            oxygen = oxygen + oxygen_supply,
            food = food + food_supply
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
        else:
            return False 




    




