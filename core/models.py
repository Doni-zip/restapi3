from django.db import models

CITY_CHOICES = [
    ('osh', 'Ош'),
    ('bishkek', 'Бишкек'),
    ('manas', 'Манас'),
    ('batken', 'Баткен'),
    ('talas', 'Талас'),
]

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    address = models.CharField(max_length=255)
    medical_info = models.TextField(max_length=2000)

    def str(self):
        return f"{self.first_name[0]}. {self.last_name} ({self.birth_date})"