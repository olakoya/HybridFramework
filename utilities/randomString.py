import random
import string

# def random_string_generate(size=5, chars=string.ascii_lowercase + string.digits):
#     return ".join(random.choice(chars) for x in range(size))"

def random_string_generate(size=8):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))