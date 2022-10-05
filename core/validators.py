

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




    # def get_connection():
    #     connection = sqlite3.connect('data_base/example.sqlite3')
    #     connection.row_factory = sqlite3.Row
    #     return connection
    #
    # @app.route('/best_selling/<int:count>')
    # def get_best_selling_tracks(count):
    #     connection = get_connection()
    #     tracks = connection.execute('SELECT * FROM best_selling_tracks').fetchmany(count)
    #     connection.close()
    #     return render_template('best_tracks.html', tracks=tracks)