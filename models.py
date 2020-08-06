from dateutil.relativedelta import relativedelta
from peewee import (
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
)

from datetime import datetime


sqlite_db = SqliteDatabase('people.db', autocommit=True)


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Location(BaseModel):
    flat = CharField(null=True)
    street_number = IntegerField()
    street_name = CharField()
    city = CharField()
    state = CharField()
    country = CharField()
    postcode = CharField()
    latitude = CharField()
    longitude = CharField()
    offset = CharField()
    description = CharField()


class Person(BaseModel):
    gender = CharField()
    title = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    date_dob = DateTimeField()
    age_dob = IntegerField()
    uuid = CharField()
    username = CharField()
    password = CharField()
    salt = CharField()
    md5 = CharField()
    sha1 = CharField()
    sha256 = CharField()
    date_registered = DateTimeField()
    age_registered = IntegerField()
    phone = IntegerField()
    cell = CharField()
    id_name = CharField(null=True)
    id_value = CharField(null=True)
    nat = CharField()
    days_left_to_birthday = IntegerField(default=0)
    location = ForeignKeyField(
        Location,
        related_name='person',
        unique=True,
        null=True
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_days_left_to_birthday(self):
        now = datetime.now()
        birthday_this_year = datetime(
            now.year,
            self.date_dob.month,
            self.date_dob.day
        )
        if now > birthday_this_year:
            next_birthday = birthday_this_year + relativedelta(year=1)
        else:
            next_birthday = birthday_this_year

        return (next_birthday - now).days

    def save(self, force_insert=False, only=None):
        # if you want to manually change days_left_to_birthday you have to
        # call something like this: person.super().save()

        # Everytime we save an instance, we automatically update the
        # days_left_to_birthday field
        self.days_left_to_birthday = self.get_days_left_to_birthday()
        super().save()

