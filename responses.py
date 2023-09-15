import random
import data


def get_response(message: str, username: str) -> str:
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

    if str(message) in data.pc_call_list:
        return pc_generator()

    if str(message) in data.i_call_list:
        return i_meter(meter)

    if str(message) in data.t_call_list:
        return t_meter(meter)

    if str(message) in data.l_call_list:
        return life_generator()

    if message == 'help':
        return data.help_print

    if message == 'kn':
        return kn()

    if message == data.choices[5]:
        return c_meter(meter)

    if message == data.choices[7]:
        return n_meter(meter)

    if message == data.choices[8]:
        return h()

    if message == data.choices[10]:
        return s_meter(meter)

    if message == 'version':
        return '```Version 0.1.1 [15.09.23]\n  New: 3 more commands including !life/lifestory```'


def pp_meter():
    meter = random.randint(1, 1000)
    character = '='
    if meter == 1000:
        return '# 8================D'
    return f'8{random.randint(0, 14)*character}D'


def poc_meter(meter):
    if meter < 10:
        return f'You are only {meter}% {data.choices[2]} :smiling_face_with_3_hearts:'
    return f'You are {meter}% {data.choices[2]}, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {meter}% {data.choices[2]}, {data.choices[0]} {data.choices[3]}'


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
    return data.slander[random.randint(0, data.slander_amount)]


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


def i_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[11]}, welcome!'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[7]}'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[8]}'
    else:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[9]}'


def t_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[10]}'
    elif 24 < meter < 50:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[11]}'
    elif 49 < meter < 95:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[12]}'
    else:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[13]}'


def life_generator():
    gender_index = random.randint(0, 1)
    age = random.randint(1, 50) if random.randint(1, 3) < 3 else random.randint(50, 119)
    iq_score = str(random.randint(60, 140) if random.randint(1, 10) <= 9 else random.randint(140, 200))
    name = data.male_names[random.randint(0, data.male_names_amount)] if gender_index == 0 else\
        data.female_names[random.randint(0, data.female_names_amount)]
    gender = data.gender(gender_index)
    country = data.countries_list[random.randint(0, data.countries_list_amount)]
    clr = data.clr_list[random.randint(0, data.clr_list_amount)]
    salary = str(salary_generator())
    job = 'Jobless' if salary == '0' else data.job_titles[random.randint(0, data.job_titles_amount)]
    debt = str(random.randint(1, 100) * random.randint(1, 100) * random.randint(1, 10))\
        if random.randint(1, 3) == 1 else '0'
    whom_in_debt = data.whom_in_debt[random.randint(0, data.whom_in_debt_amount)] if debt != '0' else 'no one'
    age_of_death = str(random.randint(age + 1, 121))
    cause_of_death = data.cause_of_death[random.randint(0, data.cause_of_death_amount)]
    return f"```Here's your character: \n Name: {name} ({gender}, {age} y/o, IQ: {iq_score}) \n Race: {clr}"\
        f" \n Country of residence: {country} \n Job: {job} \n Salary (monthly): {salary}$ \n"\
        f" Debt: {debt}$ to {whom_in_debt} \n Age of death: {age_of_death} \n Cause of death: {cause_of_death}```"


def salary_generator():
    money_seed = random.randint(1, 1000)
    final_salary = int
    if random.randint(1, 10) != 1:
        if money_seed < 50:
            final_salary = 1000 * random.randint(1, 10) / 100    # ranges from 10-100 (5%)
        if 49 < money_seed < 201:
            final_salary = 1000 * random.randint(10, 50) / 100   # ranges from 100-500 (15%)
        if 200 < money_seed < 401:
            final_salary = 1000 * random.randint(50, 100) / 100  # ranges from 500-1000 (20%)
        if 400 < money_seed < 651:
            final_salary = 1000 * random.randint(10, 25) / 10    # ranges from 1000-2500 (25%)
        if 650 < money_seed < 851:
            final_salary = 1000 * random.randint(25, 50) / 10    # ranges from 2500-5000 (20%)
        if 850 < money_seed < 926:
            final_salary = 1000 * random.randint(50, 100) / 10   # ranges from 5000-10000 (7.5%)
        if 925 < money_seed < 951:
            final_salary = 1000 * random.randint(10, 100)        # ranges from 10000-100000 (2.5%)
        if 950 < money_seed < 976:
            final_salary = 100000 * random.randint(1, 100)       # ranges from 100000-10000000 (2.5%)
        if 975 < money_seed < 990:
            final_salary = 100000 * random.randint(100, 500)     # ranges from 10000000-50000000 (1.5%)
        if money_seed > 990:
            final_salary = 1000000000 * random.randint(1, 100) / 10  # idk anymore (0.1%)
    else:
        final_salary = 0
    return int(final_salary)
