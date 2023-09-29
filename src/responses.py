import random
import data


def get_response(message: str) -> str:
    meter = int(random.randint(0, 100))

    if message in data.n_call_list:
        return poc_meter(meter)

    if message in data.l_call_list:
        return life_generator()

    if message in data.pc_call_list:
        return pc_generator()

    if message in data.c_call_list:
        return pp_meter()

    if message in data.j_call_list:
        return j_meter(meter)

    if message in data.f_call_list:
        return f_meter(meter)

    if message in data.ns_call_list:
        return slander()

    if message in data.i_call_list:
        return i_meter(meter)

    if message in data.t_call_list:
        return t_meter(meter)

    if message == 'help':
        return data.help_print

    if message == 'kn':
        return kn()

    if message == data.choices[6]:
        return c_meter(meter)

    if message == data.choices[7]:
        return n_meter(meter)

    if message == data.choices[8]:
        return h()

    if message == data.choices[10]:
        return s_meter(meter)

    if message == 'version':
        return '```Version 0.1.2 [20.09.23]\n  New: Internal optimizations & expanded dataset```'


def pp_meter():
    return f'8{random.randint(0, 14)*"="}D' if random.randint(1, 1000) != 1000 else '# 8================D'


def poc_meter(meter):
    if meter < 15:
        return f'You are only {meter}% {data.choices[2]} :smiling_face_with_3_hearts:'
    return f'You are {meter}% {data.choices[2]}, unacceptable :thumbsdown_tone1:'if meter < 50 else\
        f'You are a whopping {meter}% {data.choices[2]}, {data.choices[0]} {data.choices[3]}'


def j_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[4]} :thumbsup_tone1:'
    elif meter < 50:
        return f'You are {meter}% {data.choices[4]} :rolling_eyes:'
    elif meter < 95:
        return f'You are {meter}% {data.choices[5]} :star_of_david:'
    else:
        return data.gif1


def kn():
    return data.nresponse[random.randint(0, 6)]


def c_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[6]} :call_me:'
    elif meter < 50:
        return f'You are {meter}% {data.choices[6]} :nerd:'
    elif meter < 95:
        return f'You are {meter}% {data.choices[6]} :expressionless:'
    else:
        return f'You are {meter}% {data.choices[6]} {data.random_copypasta[0]}'


def f_meter(meter):
    if meter < 25:
        return f'You are only {meter}% {data.choices[9]} :sunglasses:'
    elif meter < 50:
        return f'You are {meter}% {data.choices[9]} :flushed:'
    elif meter < 95:
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
    elif meter < 50:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[4]}'
    elif meter < 95:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[5]}'
    else:
        return f'You are {meter}% {data.choices[10]}, {data.random_copypasta[6]}'


def i_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[11]}, welcome!'
    elif meter < 50:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[7]}'
    elif meter < 95:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[8]}'
    else:
        return f'You are {meter}% {data.choices[11]}, {data.random_copypasta[9]}'


def t_meter(meter):
    if meter < 25:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[10]}'
    elif meter < 50:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[11]}'
    elif meter < 95:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[12]}'
    else:
        return f'You are {meter}% {data.choices[12]}, {data.random_copypasta[13]}'


def life_generator():
    gender_index = random.randint(0, 1)
    age = age_generator()

    iq_score = str(random.randint(60, 120) if random.randint(1, 20) < 20 else random.randint(120, 180))

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
    final_salary = 0

    salary_ranges = {
        50: (10, 100),       # 5%
        200: (100, 500),     # 15%
        400: (500, 1000),    # 20%
        650: (1000, 2500),   # 25%
        850: (2500, 5000),   # 20%
        925: (1e3, 1e4),     # 7.5%
        950: (1e4, 1e5),     # 2.5%
        975: (1e5, 1e6),     # 2.5%
        990: (1e7, 5e7),     # 1.5%
        1000: (1e8, 1e9)     # 1%
    }

    if random.randint(1, 10) != 1:
        for seed, salary_range in salary_ranges.items():
            if money_seed <= seed:
                final_salary = random.randint(*salary_range)
                break

    return final_salary


def age_generator():
    if random.randint(1, 3) == 1:
        return random.randint(1, 15) if random.randint(1, 5) < 5 else random.randint(81, 119)
    else:
        return random.randint(16, 80)
