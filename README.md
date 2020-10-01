# Tuples

A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets


# NamedTuples
Namedtuple is a subclass of tuples and creates tuple-like immutable objects:

	```
	from collections import namedtuple
	Point2D = namedtuple('Point2D', 'x, y')
	pt1 = Point2D(20, 40)
	print(f'{pt1.x}  {pt1[0]}')
	
	```

# Functions
  I have used below function to as part fo the assignment.
  - timed
  - fake_profile_gen
  - get_larged_blood_group
  - faker_average_age
    
## fake_profile_gen
   I have used Faker package to generated fake profiles.
   
   What is faker:
   
   	`Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.`
	
1. Generated the fake profiles
2. We taking only blood_group, current_location, birthdate
3. Using namedtuples we get thse values
4. return the location details and location details
5. Return largest blood group by counting the total blood group for each type and sort them in ascending order
   get the last value which will be the highest blood group
6. Return the oldest person age min(birth_list)
	
 ```
 def fake_profile_gen(n):
    '''
       1. Generated the fake profiles
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
 
 ```

## get_larged_blood_group
   I have used collection.Counter function and sorted ascending order, while generating fake profiles
   Now here i'm getting the last record which is higher value.
   
   ```
   @timed
   def get_larged_blood_group(b_list):
       '''get the blood group in dictionary with total blood_group count and return largest one'''
       return b_list, b_list[-1][0]
   
   ```

## faker_average_age
   I have summed year, month, days indenpendently and taken mean of this value to get the average age
   ```
   @timed
   def faker_average_age(avg_birt_list):
       average_age = namedtuple('average_age', 'tm_year, tm_mon, tm_mday')
       for i in range(len(avg_birt_list)):
   	avg_age = average_age(avg_birt_list[i][0], avg_birt_list[i][1], avg_birt_list[i][2])
   	year.append(avg_age.tm_year)
   	month.append(avg_age.tm_mon)
   	day.append(avg_age.tm_mday)
       return f'{round(mean(year))}-{round(mean(month))}-{round(mean(day))}'

   ```
   


### Test Output
Local Logs

![Local Logs](https://github.com/Gaju27/session10/blob/master/pycharm_logs.JPG)

Github Action-Logs

![Github Action-Logs](https://github.com/Gaju27/session10/blob/master/action_logs.JPG)

## License
[MIT](https://choosealicense.com/licenses/mit/)

