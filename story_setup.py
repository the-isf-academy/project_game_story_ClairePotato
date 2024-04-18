from model_story import Story

main_story = Story(
    title='My First Story',
    start_id = 'start',
    start_option_title = "The start of the story.",
    start_description= "Start description."
)

main_story.add_new_child(
    parent_id = 'start', 
    child_id = 'option 1',
    child_option_title='Chose option 1',
    child_description="Option 1 description."
)






