import datetime
from collections import Counter
from collections import namedtuple
from operator import itemgetter
from statistics import mean

from faker import Faker

# Create faker object
fake = Faker()
# list of index used
fake_list = []
long_list = []
lat_list = []
blist = []
dlist = []
birth_list = []
avg_birth_list = []
year = []
month = []
day = []

today = datetime.date.today()
print(today)


def timed(fn):
    from time import perf_counter
    '''to get the average time for the function called'''

    def inner(*args, **kwargs):
        total_elapsed = 0
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        total_elapsed += (end - start)
        print('Avg Run time: {0:.6f}s  {1}'.format(total_elapsed, fn.__name__))
        return result

    return inner


@timed
def fake_profile_gen(n):
    '''1. Generated the fake profiles
       2. We taking only blood_group, current_location, birthdate
       3. Using namedtuples we get thse values
       4. return the location details and location details
       5. Return largest blood group by counting the total blood group for each type and sort them in ascending order
          get the last value which will be the highest blood group
       6. Return the oldest person age min(birth_list)
    '''
    if n > 0:
        profile_details = namedtuple('profile_details', 'blood_group current_location birthdate')
        current_location = namedtuple('current_location', 'longitude  latitude')
        for i in range(n):
            fake_list.append(fake.profile())
            sub_point = profile_details(fake_list[i]['blood_group'], fake_list[i]['current_location'],
                                        fake_list[i]['birthdate'])
            long_lat = current_location(*sub_point.current_location)
            birth_list.append(sub_point.birthdate)
            avg_birth_list.append(sub_point.birthdate.timetuple())
            long_list.append(long_lat.longitude)
            lat_list.append(long_lat.latitude)
            blist.append(fake_list[i]['blood_group'])
            dlist.append(fake_list[i]['current_location'])
    else:
        raise ValueError('Value must not be -ve, Please correct')
    return fake_list, mean(long_list), mean(lat_list), (
        sorted((Counter(blist)).items(), key=itemgetter(1))), dlist, min(birth_list), avg_birth_list


f_list, lo_list, la_list, b_list, d_list, birt_list, avg_birt_list = fake_profile_gen(10000)

print(type(len(f_list)))


@timed
def get_larged_blood_group(b_list):
    '''get the blood group in dictionary with total blood_group count and return largest one'''
    return b_list, b_list[-1][0]


@timed
def faker_average_age(avg_birt_list):
    average_age = namedtuple('average_age', 'tm_year, tm_mon, tm_mday')
    for i in range(len(avg_birt_list)):
        avg_age = average_age(avg_birt_list[i][0], avg_birt_list[i][1], avg_birt_list[i][2])
        year.append(avg_age.tm_year)
        month.append(avg_age.tm_mon)
        day.append(avg_age.tm_mday)
    return f'{round(mean(year))}-{round(mean(month))}-{round(mean(day))}'

# print('Largest blood group: ', get_larged_blood_group(b_list))
#
# print('Mean on current location: ', mean(long_list), mean(lat_list))
#
# print('Oldest person age: ', min(birt_list))
#
# print('Average_age: ',faker_average_age(avg_birt_list))
