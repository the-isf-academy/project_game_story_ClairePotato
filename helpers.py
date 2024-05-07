import sys
import time
from InquirerPy import inquirer, get_style

#Print slow
def print_slow(message,seconds):
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(seconds)
    sys.stdout.write('\n')

#Options menu
def menu(prompt, options):
    # This function creates an interactive Terminal menu.
    # it returns the selected Node 

    choice = inquirer.select(
        message= f"\n{prompt}",
        choices= options,
        qmark="",
        amark="",
        style= get_style({ 
            "answer": "#438fa8",
            "pointer": "#438fa8",
            "questionmark": "hidden"
            },
            ),
        ).execute()

    return choice