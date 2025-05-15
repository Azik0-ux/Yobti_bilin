django-admin startproject food_ordering
cd food_ordering
python manage.py startapp menu
INSTALLED_APPS = [
    # boshqa ilovalar
    'menu',
]
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name