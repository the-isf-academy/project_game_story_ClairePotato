import sys
import time

def print_slow(message,seconds):
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(seconds)
    sys.stdout.write('\n')