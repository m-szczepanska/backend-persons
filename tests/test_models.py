import datetime

import pytest
from freezegun import freeze_time

from models import Person


@pytest.fixture
def person_fixture():
    return Person(
        gender='female',
        title='Miss',
        first_name='Louane',
        last_name='Vidal',
        email='louane.vidal@example.com',
        date_dob=datetime.datetime(1966, 8, 14, 11, 50, 25, 558000),
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
        location_id=None
    )


@freeze_time("2020-08-04")
def test_check_birthday_ahead_this_year(person_fixture):
    assert person_fixture.get_days_left_to_birthday() == 10


@freeze_time("2020-08-14")
def test_check_birthday_today(person_fixture):
    assert person_fixture.get_days_left_to_birthday() == 0

# Can't directly test birthday that already happened this year due to
# freeze_time not working correctly with relativedelta
@freeze_time("2020-08-15")
def test_check_birthday_behind_this_year(person_fixture, mocker):
    relativedelta_patched = mocker.patch('models.relativedelta')
    person_fixture.get_days_left_to_birthday()
    relativedelta_patched.assert_called_once()
