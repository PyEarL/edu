def who_is_this_house_to_starks(surname):
    if surname == 'Karstark' or surname == 'Tully':
        return 'friend'
    elif surname == 'Lannister' or surname == 'Frey':
        return 'enemy'
    else:
        return 'neutral'

surname = 'yopruor'
print(who_is_this_house_to_starks(surname))