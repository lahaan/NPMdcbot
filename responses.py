import random
import niggerdump


def get_response(message: str, ) -> str:
    p_message = message.lower()

    if str(message) in niggerdump.n_call_list:
        return poc_meter()

    if str(message) in niggerdump.c_call_list:
        return cock_meter()

    if message == 'help':
        return help_commands()

    if str(message) in niggerdump.j_call_list:
        return jew_meter()

    if message == 'kn':
        return kn()

    if message == 'chink':
        return chink_meter()

    if str(message) in niggerdump.f_call_list:
        return fag_meter()

    if message == 'nazi':
        return nazi_meter()

    if message == 'hitler':
        return hitler()

    if str(message) in niggerdump.ns_call_list:
        return slander()


def cock_meter():
    meter = random.randint(0, 1000)
    character = '='
    if meter == 1000:
        return '# 8================D'
    return f'8{random.randint(0, 14)*character}D'


def poc_meter():
    meter = random.randint(0, 100)
    if meter < 10:
        return f'You are only {str(meter)}% black :smiling_face_with_3_hearts:'
    return f'You are {str(meter)}% black, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {str(meter)}% black, nigger :monkey:'


def help_commands():
    return ('```Current commands: \n !nigger [measures how black you are] \n !cock [measures your cock length] \n'
            ' !jew [measures your inner jew] \n !chink [measures your inner chink]'
            ' \n !faggot [how much of a faggot you are]\n !nazi [nazi percentage] \n !racism [says what it does] \n'
            ' [\n\n[commands also work with the prefix "pls"]```')


def jew_meter():
    meter = random.randint(0,100)
    if meter < 25:
        return f'You are {meter}% jew :thumbsup_tone1:'
    elif 24 < meter < 50:
        return f'You are {meter}% jew :rolling_eyes:'
    elif 49 < meter < 95:
        return f'You are {meter}% kike :star_of_david:'
    else:
        return ('https://media.discordapp.net/attachments/637444523861082132/'
                '965640415845941268/jew_on_radar.gif?width=160&height=160')


def kn():
    response_list = ['real', 'frfr', 'i hate niggers too', 'i also hate niggers',
                     'fuck niggers man', 'slave niggers ong', 'enslave those faggots', 'based']
    choice = random.randint(0, 7)
    return response_list[choice]


def chink_meter():
    meter = random.randint(0,100)
    if meter < 25:
        return f'You are {meter}% chink :call_me:'
    elif 24 < meter < 50:
        return f'You are {meter}% chink :nerd:'
    elif 49 < meter < 95:
        return f'You are {meter}% chink :expressionless:'
    else:
        return f'You are {meter}% chink :middle_finger: :flag_cn: #1'


def fag_meter():
    meter = random.randint(0,100)
    if meter < 25:
        return f'You are only {meter}% gay :sunglasses:'
    elif 24 < meter < 50:
        return f'You are {meter}% gay :flushed:'
    elif 49 < meter < 95:
        return f'You are {meter}% gay, so basically a faggot :thumbsdown_tone1:'
    else:
        return f'You are {meter}% gay - fucking dyke faggot :rainbow_flag:'


def nazi_meter():
    meter = random.randint(0, 100)
    return f'You are {meter}% nazi'


def hitler():
    return 'https://media.discordapp.net/attachments/637444523861082132/1134456417185710130/belovedhitler.gif'


def slander():
    return str(niggerdump.nigger_slander[random.randint(0, 50)])
