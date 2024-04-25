from model_story import Story

#Start
main_story = Story(
    title='Finding A New Home',
    start_id = 'earth',
    start_option_title = "You are at Earth.",
    start_description= "Earth is slowly becoming inhabitable. You are sent to space to search for a new planet for civilization. Be prepared to embark on your own space adventure, venturing through stars and planets."
)

#Proxima Centauri b
main_story.add_new_child(
    parent_id = 'earth', 
    child_id = 'proxima_centauri_b',
    child_option_title='Go to Unkown Planet 1',
    child_description="---"
)

#Explore planet / try to communicate with aliens  
main_story.add_new_child(
    parent_id = 'proxima_centauri_b', 
    child_id = 'communicate_with_aliens',
    child_option_title='Communicate with aliens',
    child_description="---" #aliens offer trade
)

#Trade for oxygen
main_story.add_new_child(
    parent_id = 'communicate_with_aliens', 
    child_id = 'trade_oxygen',
    child_option_title='Trade for oxygen, leave for next planet',
    child_description="---"
)

#Trade for fuel
main_story.add_new_child(
    parent_id = 'communicate_with_aliens', 
    child_id = 'trade_fuel',
    child_option_title='Trade for fuel, leave for next planet',
    child_description="---"
)

#Trade for food
main_story.add_new_child(
    parent_id = 'communicate_with_aliens', 
    child_id = 'trade_food',
    child_option_title='Trade for food, leave for next planet',
    child_description="---"
)

#Don't trade --> END
main_story.add_new_child(
    parent_id = 'communicate_with_aliens', 
    child_id = 'dominate_proxima_centauri_b',
    child_option_title="Ignore the alien's offer, stay at planet",
    child_description="You've been killed by the aliens. The game has ened."
)

#Leave Proxima Centaury B
main_story.connect_existing_child('leave_proxima_centaury_b', 'kepler_422b')

#Kepler-442b
main_story.add_new_child(
    parent_id = 'earth', 
    child_id = 'kepler_422b',
    child_option_title='Go to Unkown Planet 2',
    child_description="---"
)

#Explore Kepler-442b
main_story.add_new_child(
    parent_id = 'kepler_422b', 
    child_id = 'explore_kepler_422b',
    child_option_title='Explore planet',
    child_description="You have been exploring for a while and you've encounted a bit of flora and fauna, but your oxygen supply is running low. You can head back to spaceship but you might not be able to find this area again, do you want to continue exploring?"
)

#Continue exploring Kepler-442b --> END
main_story.add_new_child(
    parent_id = 'explore_kepler_422b', 
    child_id = 'explore_kepler_422b_2',
    child_option_title='Continue exploring planet',
    child_description="You have run out of oxygen, the game has ended"
)

#Kepler-442b back to spaceship
main_story.add_new_child(
    parent_id = 'explore_kepler_422b', 
    child_id = 'back_to_spaceship',
    child_option_title='Headback to spaceship',
    child_description="You've safely returned back to the spaceship and have refilled your oxygen supply. You can either go back to exploring, stay at the spaceship, go back to the previous planet, or try exploring another planet."
)

#Kepler-442b stay at spaceship --> END
main_story.add_new_child(
    parent_id = 'back_to_spaceship', 
    child_id = 'stay_at_spaceship',
    child_option_title='Stay at spaceship',
    child_description="You've lost track of time and stayed at your spaceship for too long . Your food supply has ran out. The game has ended."
)

#Kepler-442b back to Proxima Centauri B --> END
main_story.add_new_child(
    parent_id = 'back_to_spaceship', 
    child_id = 'leave_kepler_422b_2',
    child_option_title=' Go back to Unkown planet 1 (Proxima Centauri b)',
    child_description="You ran out of fuel on the way. The game has ended."
)

#Kepler-442b leave for Unkown Planet 3 --> END
main_story.add_new_child(
    parent_id = 'back_to_spaceship', 
    child_id = 'leave_kepler_422b_3',
    child_option_title='Leave for Unkown planet 3 ',
    child_description="You encountered a black hole on the way to Unknown planet 3. The game has eneded."
)

#Kepler-442b back to exploring
main_story.add_new_child(
    parent_id = 'back_to_spaceship', 
    child_id = 'explore_kepler_422b_3',
    child_option_title='Continue exploring planet',
    child_description="You've experiened extreme temperature fluctuations, but besides that the planet seems habitable. You've also discovered a region with suitable conditions after weeks of exploration. Do you want to try starting a civilization at planet Kepler 422b?"
)

#Settle at Kepler 422b
main_story.add_new_child(
    parent_id = 'explore_kepler_422b_3', 
    child_id = 'settle_kepler_422b',
    child_option_title='Settle at Kepler 422b',
    child_description="Congratulations, you've successfully started a civillization at planet Kepler 422b!"
)

#Quit
main_story.add_new_child(
    parent_id = 'settle_kepler_422b', 
    child_id = 'quit',
    child_option_title='Quit game',
    child_description="The game has ended"
)

#Play again
main_story.add_new_child(
    parent_id = 'settle_kepler_422b', 
    child_id = 'play_again',
    child_option_title='Play again',
    child_description="Okay, you're being sent back to the start of the game..."
)

#Kepler-62f
main_story.add_new_child(
    parent_id = 'earth', 
    child_id = 'kepler_62f',
    child_option_title='Go to Unkown Planet 3',
    child_description="---"
)

#Explore Kepler 62f
main_story.add_new_child(
    parent_id = 'kepler_62f', 
    child_id = 'explore_kepler_62f',
    child_option_title='Explore planet',
    child_description="You've been exploring for a while and are running low on food. You could try the mushroom looking organisms around you or head back to the spaceship."
)

#Kepler 62f back to spaceship --> END
main_story.add_new_child(
    parent_id = 'explore_kepler_62f', 
    child_id = 'kepler_62f_back_to_spaceship',
    child_option_title='Headback to spaceship',
    child_description="You've ran out of oxygen supply on the way back to the spaceship. The game has ended"
)

#Kepler 62f eat mushrooms --> END
main_story.add_new_child(
    parent_id = 'explore_kepler_62f', 
    child_id = 'eat_mushroom',
    child_option_title='Try eating the mushroom',
    child_description="The mushrooms turned out to be poisonous. The game has ended."
)