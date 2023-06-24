from datetime import timedelta

# https://djangoproject.com

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


#  1 cat -------> Many conf
#  1 conf ------> 1 cat:


class Conference(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

def __str__(self):
        return self.name

# creating dummy data for conferences app
create_dummy_conferences():
    for i in range(10):
        Conference.objects.create(
            name=f"Conference {i}",
            category="Category",
            date=date(2023, 6, 1),
            venue="Venue",
            theme="Theme"
        )

create_dummy_conferences()