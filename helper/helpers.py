import random
import string


def get_random_text():
    digits = "".join([random.choice(string.digits) for i in range(8)])
    chars = "".join([random.choice(string.ascii_letters) for i in range(15)])
    return digits + chars
