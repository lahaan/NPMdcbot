import random
import data


def get_response(message: str, ) -> str:
    meter = int(random.randint(0, 100))

    if str(message) in data.n_call_list:
        return poc_meter(meter)

    if str(message) in data.c_call_list:
        return pp_meter()

    if str(message) in data.j_call_list:
        return j_meter(meter)

    if str(message) in data.f_call_list:
        return f_meter(meter)

    if str(message) in data.ns_call_list:
        return slander()

    if str(message) in data.pc_cal_list:
        return pc_generator()

    if message == 'help':
        return data.help_print

    if message == 'kn':
        return kn()

    if message == data.choices[5]:
        return c_meter(meter)

    if message == data.choices[6]:
        return n_meter(meter)

    if message == data.choices[7]:
        return h()

    if message == data.choices[10]:
        return s_meter(meter)

    if message == 'version':
        return '```Version 0.1.0 [13.09.23]\n  New: Data rework, optimizations, !soy```'


def pp_meter():
    meter = random.randint(1, 1000)
    character = '='
    if meter == 1000:
        return '# 8================D'
    return f'8{random.randint(0, 14)*character}D'


def poc_meter(meter):
    if meter < 10:
        return f'You are only {str(meter)}% {data.choices[2]} :smiling_face_with_3_hearts:'
    return f'You are {str(meter)}% {data.choices[2]}, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {str(meter)}% {data.choices[2]}, {data.choices[0]} {data.choices[3]}'


def j_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[4]} :thumbsup_tone1:'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[4]} :rolling_eyes:'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[5]} :star_of_david:'
    else:
        return data.gif1


def kn():
    return data.nresponse[random.randint(0, 6)]


def c_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[6]} :call_me:'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[6]} :nerd:'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[6]} :expressionless:'
    else:
        return f'You are {meter}% {data.choices[6]} {data.random_copypasta[0]}'


def f_meter(meter):
    if meter < 25:
        return f'You are only {meter}% {data.choices[9]} :sunglasses:'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[9]} :flushed:'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[9]}, {data.random_copypasta[1]}'
    else:
        return f'You are {meter}% {data.choices[9]} - {data.random_copypasta[2]}'


def n_meter(meter):
    return f'Your {data.choices[7]} meter is: {(meter // 10) * data.mote}'


def h():
    return data.gif2


def slander():
    return str(data.slander[random.randint(0, data.slander_amount)])


def pc_generator():
    return (f'```Your spec: \n CPU: {data.cpu_list[random.randint(0, data.cpu_list_amount)]}\n'
            f' GPU: {data.gpu_list[random.randint(0, data.gpu_list_amount)]}\n'
            f' PSU: {data.psu_brand[random.randint(0, data.psu_brand_amount)]}'
            f' {random.randint(10, 20) if random.randint(1, 3) == 1 else random.randint(2, 9)}00W'
            f' {data.psu_tier[random.randint(0, data.psu_tier_amount)]}\n'
            f' RAM: {data.ram_sizes[random.randint(0, data.ram_sizes_amount)]}'
            f' {data.ram_tuning[random.randint(0, 2)]}\n'
            f' Storage: {storage()}\n'
            f' Cooling: {cooling()}\n'
            f' Case: {data.case_brand[random.randint(0, data.case_brand_amount)]}'
            f' {data.case_sizes[random.randint(0, data.case_sizes_amount)]}```')


def cooling():
    if random.randint(1, 2) == 1:  # water cooling 50%
        if random.randint(1, 2) == 1:  # custom water cooling 50%*50%
            return f'{data.rad_sizes[random.randint(0, data.rad_sizes_amount)]} custom water cooling'
        return f'{data.aio_coolers[random.randint(0, data.aio_coolers_amount)]}'
    return f'{data.air_coolers[random.randint(0, data.air_coolers_amount)]}'  # air cooling 50%


def storage():
    if random.randint(1, 2) == 1:  # HDD
        return (f'{data.storage_sizes[random.randint(0, data.storage_sizes_amount)]}'
                f' {data.hdd_rpm[random.randint(0, 2)]} HDD')
    return (f'{data.storage_sizes[random.randint(0, data.storage_sizes_amount)]}'
            f' {data.ssd_cell_level[random.randint(0, data.ssd_cell_level_amount)]} SSD {dram_cache()}')


def dram_cache():
    return 'w/ DRAM cache' if random.randint(1, 2) == 1 else ''


def s_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[10]}, based'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[4]}'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[5]}'
    else:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[6]}'
