import random
import string

def generate_password(len = 12):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ( random.choice(string.ascii_lowercase) +random.choice(string.ascii_uppercase) + random.choice(string.digits) +random.choice(string.punctuation))
    password += ''.join(random.choice(characters) for _ in range(len-4))
    return password



print(f"password : {generate_password()}")