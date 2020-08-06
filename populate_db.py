from datetime import datetime
import json

from models import Person, Location


def populate_location(person):
    try:
        # in case people would live in flats as well
        flat=person['location']['street']['flat']
    except KeyError:
        flat = ''
    person_location = Location.create(
        flat=flat,
        street_number=int(person['location']['street']['number']),
        street_name=person['location']['street']['name'],
        city=person['location']['city'],
        state=person['location']['state'],
        country=person['location']['country'],
        postcode=person['location']['postcode'],
        latitude=person['location']['coordinates']['latitude'],
        longitude=person['location']['coordinates']['longitude'],
        offset=person['location']['timezone']['offset'],
        description=person['location']['timezone']['description']
    )
    return person_location


def populate_person(person, phone_num, person_location=None):
    if not person_location:
        person_location = populate_location(person)
    new_person = Person.create(
        gender=person['gender'],
        title=person['name']['title'],
        first_name=person['name']['first'],
        last_name=person['name']['last'],
        email=person['email'],
        uuid=person['login']['uuid'],
        username=person['login']['username'],
        password=person['login']['password'],
        salt=person['login']['salt'],
        md5=person['login']['md5'],
        sha1=person['login']['sha1'],
        sha256=person['login']['sha256'],
        date_dob=datetime.fromisoformat(person['dob']['date'][:10]),
        age_dob=int(person['dob']['age']),
        date_registered=datetime.fromisoformat(
            person['registered']['date'][:10]
        ),
        age_registered=int(person['registered']['age']),
        phone=phone_num,
        cell=person['cell'],
        id_name=person['id']['name'],
        id_value=person['id']['value'],
        nat=person['nat'],
        location=person_location
    )
    return new_person


def normalize_phone_num(person):
    phone_num = person['phone']
    if not phone_num.isdigit():
        phone_num = int(''.join([x for x in phone_num if x.isdigit()]))
    return phone_num


def create_fields():
    with open('data/persons.json') as file:
        data = json.load(file)
        persons_fields = data['results']

        for person in persons_fields:
            phone_num = normalize_phone_num(person)
            populate_person(
                person,
                phone_num,
                person_location=None
            )


create_fields()
