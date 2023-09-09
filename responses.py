import random
import niggerdump


def get_response(message: str, ) -> str:
    meter = int(random.randint(0, 100))

    if str(message) in niggerdump.n_call_list:
        return poc_meter(meter)

    if str(message) in niggerdump.c_call_list:
        return cock_meter()

    if str(message) in niggerdump.j_call_list:
        return jew_meter(meter)

    if str(message) in niggerdump.f_call_list:
        return fag_meter(meter)

    if str(message) in niggerdump.ns_call_list:
        return slander()

    if str(message) in niggerdump.pc_cal_list:
        return pc_generator()

    if message == 'help':
        return help_commands()

    if message == 'kn':
        return kn()

    if message == 'chink':
        return chink_meter(meter)

    if message == 'nazi':
        return nazi_meter(meter)

    if message == 'hitler':
        return hitler()

    if message == 'version':
        return '```Version 0.0.5 [08.09.23]\n  New: 0.0.5 brings !pc```'


def cock_meter():
    meter = random.randint(1, 1000)
    character = '='
    if meter == 1000:
        return '# 8================D'
    return f'8{random.randint(0, 14)*character}D'


def poc_meter(meter):
    if meter < 10:
        return f'You are only {str(meter)}% black :smiling_face_with_3_hearts:'
    return f'You are {str(meter)}% black, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {str(meter)}% black, nigger :monkey:'


def help_commands():
    return ('```Current commands: \n !nigger [measures how black you are] \n !cock [measures your cock length] \n'
            ' !jew [measures your inner jew] \n !chink [measures your inner chink]'
            ' \n !faggot [how much of a faggot you are]\n !nazi [nazi bar] \n !racism [says what it does] \n'
            ' !pc [Your PC randomly generated] \n\n[commands also work with the prefix "pls"]```')


def jew_meter(meter):
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
    choice = random.randint(0, 6)
    return response_list[choice]


def chink_meter(meter):
    if meter < 25:
        return f'You are {meter}% chink :call_me:'
    elif 24 < meter < 50:
        return f'You are {meter}% chink :nerd:'
    elif 49 < meter < 95:
        return f'You are {meter}% chink :expressionless:'
    else:
        return f'You are {meter}% chink :middle_finger: :flag_cn: #1'


def fag_meter(meter):
    if meter < 25:
        return f'You are only {meter}% gay :sunglasses:'
    elif 24 < meter < 50:
        return f'You are {meter}% gay :flushed:'
    elif 49 < meter < 95:
        return f'You are {meter}% gay, so basically a faggot :thumbsdown_tone1:'
    else:
        return f'You are {meter}% gay - fucking dyke faggot :rainbow_flag:'


def nazi_meter(meter):
    return f'Your nazi meter is: {(meter // 10) * "卐"}'


def hitler():
    return 'https://media.discordapp.net/attachments/637444523861082132/1134456417185710130/belovedhitler.gif'


def slander():
    return str(niggerdump.nigger_slander[random.randint(0, 49)])


def pc_generator():
    return (f'```Your spec: \n CPU: {niggerdump.cpu_list[random.randint(0, 291)]}\n'
            f' GPU: {niggerdump.gpu_list[random.randint(0, 189)]}\n'
            f' PSU: {niggerdump.psu_brand[random.randint(0, 21)]}'
            f' {random.randint(10, 20) if random.randint(1, 3) == 1 else random.randint(2, 9)}00W'
            f' {niggerdump.psu_tier[random.randint(0, 6)]}\n'
            f' RAM: {ram()}\n'
            f' Storage: {storage()}\n'
            f' Cooling: {cooling()}\n'
            f' Case: {niggerdump.case_brand[random.randint(0, 32)]} {niggerdump.case_sizes[random.randint(0, 6)]}```')


def cooling():
    if random.randint(1, 2) == 1:  # water cooling 50%
        if random.randint(1, 2) == 1:  # custom water cooling 50%*50%
            return f'{niggerdump.rad_sizes[random.randint(0, 9)]} custom water cooling'
        return f'{niggerdump.aio_coolers[random.randint(0, 5)]}'
    return f'{niggerdump.air_coolers[random.randint(0, 34)]}'  # air cooling 50%


def storage():
    if random.randint(1, 2) == 1:  # HDD
        return f'{niggerdump.storage_sizes[random.randint(0, 9)]} {niggerdump.hdd_rpm[random.randint(0, 2)]} HDD'
    return (f'{niggerdump.storage_sizes[random.randint(0, 9)]} {niggerdump.ssd_cell_level[random.randint(0, 4)]}'
            f' SSD {dram_cache()}')


def ram():
    return f'{niggerdump.ram_sizes[random.randint(0, 11)]} {niggerdump.ram_tuning[random.randint(0, 2)]}'


def dram_cache():
    return 'w/ DRAM cache' if random.randint(1, 2) == 1 else ''
