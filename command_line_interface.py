import argparse
from collections import Counter
from datetime import datetime

import re

from models import Person, Location
from calculate_password_points import get_best_passwords

# female percentage in population
def female_percentage():
    p_all = Person.select()
    p_female = Person.select().where(Person.gender == 'female')
    percentage_female = round((len(p_female)/len(p_all) * 100), 2)
    print(f'{percentage_female}%')

# male percentage in population
def male_percentage():
    p_all = Person.select()
    p_male = Person.select().where(Person.gender == 'male')
    percentage_male = round((len(p_male)/len(p_all) * 100), 2)
    print(f'{percentage_male}%')

# female average age in population
def female_age_average():
    p_female = Person.select().where(Person.gender == 'female')
    p_female_list = [x.age_dob for x in p_female]
    age_average = sum(p_female_list)/len(p_female_list)
    print(round(age_average, 2))

# male average age in population
def male_age_average():
    p_male = Person.select().where(Person.gender == 'male')
    p_male_list = [x.age_dob for x in p_male]
    age_average = sum(p_male_list)/len(p_male_list)
    print(round(age_average, 2))

# people average age in population
def people_age_average():
    p_all = Person.select()
    p_all_list = [x.age_dob for x in p_all]
    age_average = sum(p_all_list)/len(p_all_list)
    print(round(age_average, 2))

# 'N' most popular cities
def most_popular_cities(n):
    locations = Location.select()
    cities_list = [elem.city for elem in locations]
    city_counter = Counter()
    for city in cities_list:
        city_counter[city] += 1
        print(city_counter.most_common(n))

# 'N' most common passwords
def most_common_password(n):
    persons = Person.select()
    pass_dict = [person.password for person in persons]
    password_counter = Counter()
    for password in pass_dict:
        password_counter[password] += 1
    for popular_password in password_counter.most_common(n):
        print(f'Password "{popular_password[0]}" occured {popular_password[1]}')

# People born before date_before and after date_after
def show_people_born_before_and_after_date(date_before, date_after):
    date_before_datetime = datetime.fromisoformat(date_before)
    date_after_datetime = datetime.fromisoformat(date_after)
    persons_query = (Person
        .select()
        .where(
            (Person.date_dob < date_before_datetime)
            | (Person.date_dob > date_after_datetime)
        )
    )
    persons = [elem for elem in persons_query]
    print(persons)

# People born beetwen dates date_before, date_after
def show_people_born_between_dates(date_before, date_after):
    date_before_datetime = datetime.fromisoformat(date_before)
    date_after_datetime = datetime.fromisoformat(date_after)
    persons_query = (Person
        .select()
        .where(
            Person.date_dob.between(date_after_datetime, date_before_datetime)
        )
    )
    persons = [elem for elem in persons_query]
    import pdb; pdb.set_trace()
    print(persons)


parser = argparse.ArgumentParser(description='Show results.')

subparsers = parser.add_subparsers()
parser_female_percentage = subparsers.add_parser('female_percentage', help='female percentage')
parser_female_percentage.set_defaults(func=female_percentage)

parser_male_percentage = subparsers.add_parser('male_percentage', help='male percentage')
parser_male_percentage.set_defaults(func=male_percentage)

parser_female_age_average = subparsers.add_parser('female_age_average', help='average female age in the population')
parser_female_age_average.set_defaults(func=female_age_average)

parser_male_age_average = subparsers.add_parser('male_age_average', help='average male age in the population')
parser_male_age_average.set_defaults(func=male_age_average)

parser_people_age_average = subparsers.add_parser('people_age_average', help='average age in the population')
parser_people_age_average.set_defaults(func=people_age_average)

parser_most_common_password = subparsers.add_parser('most_common_password', help='most common password')
parser_most_common_password.add_argument('n', type=int, help='how many passwords do you want to get')
parser_most_common_password.set_defaults(func=most_common_password)

parser_show_people_born_before_and_after_date = subparsers.add_parser('show_people_born_before_and_after_date', help='most common password')
parser_show_people_born_before_and_after_date.add_argument('date_before', type=str, help='insert date before birthday in YYYY-MM-DD format')
parser_show_people_born_before_and_after_date.add_argument('date_after', type=str, help='insert date after birthday in YYYY-MM-DD format')
parser_show_people_born_before_and_after_date.set_defaults(func=show_people_born_before_and_after_date)

parser_show_people_born_between_dates = subparsers.add_parser('show_people_born_between_dates', help='show people born between given dates')
parser_show_people_born_between_dates.add_argument('date_after', type=str, help='insert date after birthday in YYYY-MM-DD format')
parser_show_people_born_between_dates.add_argument('date_before', type=str, help='insert date before birthday in YYYY-MM-DD format')
parser_show_people_born_between_dates.set_defaults(func=show_people_born_between_dates)

parser_best_password = subparsers.add_parser('get_best_passwords', help='show passwords with the highest poinst value')
parser_best_password.set_defaults(func=get_best_passwords)



options = parser.parse_args()

if options.func.__name__ == 'show_people_born_before_and_after_date' or options.func.__name__ == 'show_people_born_between_dates':
    options.func(options.date_before, options.date_after)
elif options.func.__name__ == 'most_common_password' or options.func.__name__ == 'most_popular_cities':
    options.func(options.n)
else:
    options.func()

