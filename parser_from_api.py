from requests import get
import json

from populate_db import normalize_phone_num, populate_person


def parse_data_from_api():
    # Get 1000 randomly choosen people, as in person.json file
    response = get('https://randomuser.me/api/?results=1000')
    # Try to get any content from given url
    try:
        data = json.loads(response.text)
    except response.status_code != 200:
        return 'Data not found.'

    persons_fields = data['results']

    for person in persons_fields:
        phone_num = normalize_phone_num(person)
        populate_person(
            person,
            phone_num,
            person_location=None
        )


parse_data_from_api()
