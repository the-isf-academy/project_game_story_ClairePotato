class Node():
    def __init__(self, id, option_title, description, fuel_supply, oxygen_supply, food_supply):
        # initializes a node object with its properties
        
        self.id = id # a unique id
        self.children = []  #a list of node objects
        self.option_title = option_title  # text for display in the menu          
        self.description = description  # text to show if this option is selected 
        self.fuel_supply = fuel_supply
        self.oxygen_supply = oxygen_supply
        self.food_supply = food_supply

    def __str__(self):
        # defines how a node will be printed 

        return f"{self.option_title}"

    def add_child(self, child_node):
        # adds a new child node to a node

        self.children.append(child_node)
    
    def find(self, id, seen=None):
        # 🚨 DO NOT EDIT THIS METHOD 🚨
        # It searches through the nodes to return the node with the given id
        # It uses a fancy technique called recursion to find the correct node
        # If you're interested in learning more, ask a teacher! 
        
        if self.id == id: 
            return self
        
        # adding seen to prevent infinite looping
        if seen == None:
            seen = [] 
        seen.append(self.id)
        
        for child in self.children:
            if child.id not in seen:
                n = child.find(id, seen)
                if n: 
                    return n
        return None 
    
