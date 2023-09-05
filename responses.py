import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if message == 'nice':
        meter = random.randint(0, 100)
        return poc_meter()

    if message == 'cock':
        character = '='
        return cock_meter()


def cock_meter():
    character = '='
    return f'8{random.randint(1, 10)*character}D'


def poc_meter():
    meter = random.randint(0, 100)
    return f'You are {str(meter)}% black, good enough :thumbsup_tone1:' if meter < 50 else\
        f'You are {str(meter)}% black,  :thumbsdown_tone1:'
