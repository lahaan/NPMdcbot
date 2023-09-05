import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if message == 'nigger':
        return str(random.randint(1, 100))

    return 'ion geddit'
