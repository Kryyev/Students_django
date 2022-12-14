from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker


from core.validators import ValidEmailDomain, ValidateUniqueEmail, CleanLastName, CleanFirstName, CleanPhone

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@icloud.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols'), CleanFirstName]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2), CleanLastName],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), ValidateUniqueEmail])
    phone = models.CharField(max_length=20, validators=[CleanPhone])

    def __str__(self):
        return f'{self.pk} {self.first_name} {self.last_name} {self.phone}'

    def __str__(self):
        return relativedelta(date.today(), self.birthday).years

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            phone = f.phone()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email, phone=phone)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print(f'Incorrect data {first_name}, {last_name}, {email}, {birthday} {phone}')
