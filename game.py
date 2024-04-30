from story_setup import main_story # stores the Story object in main_story
from view import View

view = View() # creates a View object
         

# show the start message
view.start_game(main_story)

# main game loop, runs until story is finished
while main_story.is_finished() == False:    
    chosen_node = view.menu("[what will you do?]", main_story.get_current_children())
    main_story.set_current_node(chosen_node)
    main_story.add_fuel_supply(chosen_node.fuel_supply)
    main_story.add_oxygen_supply(chosen_node.oxygen_supply)
    main_story.add_food_supply(chosen_node.food_supply)
    if main_story.fuel_supply < 0:
        view.end_game()
    elif main_story.oxygen_supply < 0:
        view.end_game()
    elif main_story.food_supply < 0:
        view.end_game()
    view.show_node_description(chosen_node)
    view.show_supply_stats(main_story.fuel_supply, main_story.oxygen_supply, main_story.food_supply)

# show the end message
view.end_game()




