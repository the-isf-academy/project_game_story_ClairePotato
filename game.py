from story_setup import main_story # stores the Story object in main_story
from view import View
from helpers import menu
from snake2 import*

view = View() # creates a View object
         

# show the start message
view.start_game(main_story)

while True:
    # main game loop, runs until story is finished
    while main_story.is_finished() == False:    
        print(main_story.get_current_children())
        chosen_node = view.menu("[what will you do?]", main_story.get_current_children())
        main_story.set_current_node(chosen_node)
        view.show_node_description(chosen_node)
        view.show_supply_stats(main_story.fuel_supply, main_story.oxygen_supply, main_story.food_supply)
        main_story.add_fuel_supply(chosen_node.fuel_supply)
        main_story.add_oxygen_supply(chosen_node.oxygen_supply)
        main_story.add_food_supply(chosen_node.food_supply)
        if main_story.current_node.id == "snake_game":
            the_snake_game = Snake()
            the_snake_game.snake_game()
            win_time = the_snake_game.total_time
            if win_time == None or win_time > 10:
                # if player took more than the time limit to beat the game
                print("You suck at the snake game.")
                break
            elif the_snake_game.win == False: 
                # if player loose eg. snake crashed with itself
                print("You suck at the snake game.")
                break

    # show the end message
    view.end_game(main_story)
    options = ["Play again", "Quit"]
    option = menu("Menu", options)
    if option == "Play again":
        main_story.reset_supplies()
        main_story.set_current_node(main_story.first_node)
    else:
        quit()



