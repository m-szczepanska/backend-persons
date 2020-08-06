import re

from models import Person


# Special chars list: https://randomuser.me/documentation#format
re_pattern_special_char = r'[!"#$%&()\*\+\,\- \./:;<=>?@[\]\^_`\{\|\}~]+'
re_pattern_length_8 = r'.{8,}'
re_pattern_uppercase = r'[A-Z]+'
re_pattern_lowercase = r'[a-z]+'
re_pattern_digit = r'[0-9]+'


def get_all_passwords_points():
    persons = Person.select()
    pass_set = set([person.password for person in persons])
    password_points = {}
    for password in pass_set:
        points = count_points_in_password(password)
        if points not in password_points:
            password_points[points] = []
        password_points[points].append(password)
    return password_points


def count_points_in_password(password):
    points = 0
    if re.search(re_pattern_length_8, password):
        points += 5
    if re.search(re_pattern_special_char, password):
        points += 3
    if re.search(re_pattern_uppercase, password):
        points += 2
    if re.search(re_pattern_lowercase, password):
        points += 1
    if re.search(re_pattern_digit, password):
        points += 1
    return points


def get_best_passwords():
    best_passwords = get_all_passwords_points()
    max_points = max(best_passwords.keys())
    print(f'{max_points} points passwords: {best_passwords[max_points]}')