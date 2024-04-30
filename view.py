from InquirerPy import inquirer, get_style  
from helpers import print_slow     
from playsound import playsound

class View:

    def menu(self, prompt, options):
        # This function creates an interactive Terminal menu.
        # it returns the chosen ption 

        choice = inquirer.select(
            message= f"{prompt}",
            choices= options,
            qmark="",
            amark="",
            style= get_style({ 
                "answer": "#438fa8",
                "pointer": "#438fa8",
                "questionmark": "hidden"},

                ),
            ).execute()

        return choice

    def start_game(self, story):
        print("="*50)
        print(f"Title: {story.title}")
        print(f"{story.first_node.option_title}")
        print(f"{story.first_node.description}", 0.03)
        print("="*50)

    def show_node_description(self, node):
        print(f"{node.description}", 0.05)
    
    def show_supply_stats(self, fuel_supply, oxygen_supply, food_supply):
        print(f"""
              
-----STATS-----
Fuel Supply: {fuel_supply}
Oxygen Supply: {oxygen_supply}
Food Supply: {food_supply}""")
        print("-"*15)

    def end_game(self):
        print("="*50)
        print("""\
                                _ 
 ___ ___ _____ ___    ___ ___ _| |
| . | .'|     | -_|  | -_|   | . |
|_  |__,|_|_|_|___|  |___|_|_|___|
|___|                             """)
        playsound("Arcade game over sound effect!.mp3")
        print("="*50)