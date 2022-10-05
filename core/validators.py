import re

import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import sqlite3


def get_connection():
    connection = sqlite3.connect('../db.sqlite3')
    connection.row_factory = sqlite3.Row
    return connection


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <{args[0].split("@")[1]}> not valid.')


@deconstructible
class ValidateUniqueEmail:
    def UniqueEmail(self, value):
        connection = get_connection()
        email = connection.execute('Select email from students')
        if email == value:
            raise 'Email is already taken.'
        else:
            pass


@deconstructible
class CleanFirstName:
    def FNClean(self, value):
        cleanf = value[0].apper() + value[1:].lover()
        return cleanf


@deconstructible
class CleanLastName:
    def LNclean(self, value):
        cleanl = value[0].apper() + value[1:].lover()
        return cleanl


@deconstructible()
class CleanPhone:
    def CleanPhone(self, value):
        reg = re.compile('\d')
        return reg
