import random


def get_response(message: str, ) -> str:
    p_message = message.lower()

    if message == 'nice':
        return poc_meter()

    if message == 'cock':
        character = '='
        return cock_meter()

    if message == 'help':
        return help_meter()

    if message == 'star':
        return star_meter()

    if message == 'kn':
        return kn()



def cock_meter():
    character = '='
    return f'8{random.randint(0, 14)*character}D'


def poc_meter():
    meter = random.randint(0, 100)
    if meter < 10:
        return f'You are only {str(meter)}%  nice:smiling_face_with_3_hearts:'
    return f'You are {str(meter)}% nice, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {str(meter)}% , nice:'


def help_meter():
    return ('```Current commands: \n !nice [] \n !cock [measures your cock length] \n'
            ' !star []```')


def star_meter():
    meter = random.randint(0,100)
    if meter < 25:
        return f'You are {meter}% star :thumbsup_tone1:'
    elif 24 < meter < 50:
        return f'You are {meter}% star :rolling_eyes:'
    elif 49 < meter < 95:
        return f'You are {meter}% star :star_of_david:'
    else:
        return ('https://media.discordapp.net/attachments/637444523861082132/'
                '965640415845941268/jew_on_radar.gif?width=160&height=160')


def kn():
    response_list = ['choice1', 'choice2']
    choice = random.randint(0, 7)
    return response_list[choice]
