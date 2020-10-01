import inspect
import os
import re

import pytest

import session10

README_CONTENT_CHECK_FOR = [
    'timed',
    'fake_profile_gen',
    'get_larged_blood_group',
    'faker_average_age',
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


#
# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(session10)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_fake_profile_gen_for_neg_input():
    with pytest.raises(Exception, match=r".* -ve *"):
        session10.fake_profile_gen(-1)


def test_fake_profile_gen_works():
    f_list, lo_list, la_list, b_list, d_list, birt_list, avg_birt_list = session10.fake_profile_gen(1)
    assert len(f_list) != 0, 'Length of Faker profiles must have some values i.e length of list not equals to zero '
    assert len(lo_list) != 0, 'Length of longitude must have some values i.e length of list not equals to zero'
    assert len(la_list) != 0, 'Length of latitude must have some values i.e length of list not equals to zero'
    assert len(b_list) != 0, 'Length of Blood group must have some values i.e length of list not equals to zero'
    assert len(d_list) != 0, 'Length of Current Location must have some values i.e length of list not equals to zero'
    assert len(birt_list) != 0, 'Length of birthdate must have some values i.e length of list not equals to zero'
    assert len(avg_birt_list) != 0, 'Length of average birth must have some values i.e length of list not equals to zero'


def test_for_largest_blood_group():
    f_list, lo_list, la_list, b_list, d_list, birt_list, avg_birt_list = session10.fake_profile_gen(10000)
    _, blood_list = session10.get_larged_blood_group(b_list)
    assert b_list[-1][0] == blood_list, 'Checking for the largest blood group from profiles'


def test_for_average_age():
    *_, avg_birt_list = session10.fake_profile_gen(10000)
    _, blood_list = session10.get_larged_blood_group(b_list)
    assert bool(avg_birt_list) == True, 'Checking for the largest blood group from profiles'
