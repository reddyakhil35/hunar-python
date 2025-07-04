import random
import string

def captcha(length=5):
    characters = string.ascii_letters + string.digits
    captchagenerator = ""
    for _ in range(length):
        captchagenerator += random.choice(characters)
    return captchagenerator

# Example usage
captchagenerator= captcha()
print(captchagenerator)
