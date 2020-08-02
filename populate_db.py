import datetime

from models import Person, Location


def create_location():
    new_location = Location.create(
        flat='',
        street_number=12,
        street_name='penny lane',
        city='oslo',
        state='status',
        country='poland',
        postcode=52235,
        latitude='2.0565',
        longitude='95.2422',
        offset='+1:00',
        description='a nice location'
    )
    return new_location


def create_test_person(location=None):
    if not location:
        location = create_location()
    new_person = Person.create(
        gender='female',
        title='Miss',
        first_name='Louane',
        last_name='Vidal',
        email='louane.vidal@example.com',
        date_dob=datetime.datetime(1966, 6, 26, 11, 50, 25, 558000),
        age_dob=54,
        uuid='9f07341f-c7e6-45b7-bab0-af6de5a4582d',
        username='angryostrich988',
        password='r2d2',
        salt='B5ywSDUM',
        md5='afce5fbe8f32bcec1a918f75617ab654',
        sha1='1a5b1afa1d9913cf491af64ce78946d18fea6b04',
        sha256='1a5b1afa1d9913cf491af64ce78946d18fea6b04',
        date_registered=datetime.datetime(1969, 6, 26, 11, 50, 25, 558000),
        age_registered=3,
        phone=666777888,
        cell=45454,
        id_name='INSEE',
        id_value='fd7s9f',
        nat='FR',
        location_id=location.id
    )
    return new_person
