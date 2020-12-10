from django.db import models

from articles.models import Articles
# Create your models here.

class Container(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity", default=1)

    def __str__(self):
        return self.articles.title

class Panner_Articles(models.Model):
    container = models.ManyToManyField(Container)
    date_add = models.DateTimeField("Add at", auto_now=True)

class Panner(models.Model):
    user_cookies = models.CharField("User cookies", max_length=255, unique=True)
    panner = models.ForeignKey(Panner_Articles, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_cookies