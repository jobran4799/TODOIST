import random
import string

class Utiles():
    def generate_random_string(length=10):
        """Generate a random string of specified length."""
        # Define the characters to choose from
        characters = string.ascii_letters
        # Generate the random string
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
