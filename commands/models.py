from django.db import models

from articles.models import Articles
# Create your models here.

class Articles_On_Panner(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField("Quantity", default=1)
    
    def __str__(self):
        return self.articles.title

class Panner(models.Model):
    articles = models.ManyToManyField(Articles_On_Panner, related_name="Articles")
    user_cookies = models.CharField("User cookies", max_length=255, unique=True)

    def __str__(self):
         return self.user_cookies


class Client(models.Model):
    last_name = models.CharField("Last name", max_length=40, blank=True)
    first_name = models.CharField("First name", max_length=40, blank=True)
    email = models.EmailField("Email", max_length=30, unique=True)
    telephone = models.CharField("Telephone", max_length=20, unique=True)
    address = models.TextField("Address", blank=True)

    def __str__(self):
        if self.last_name and self.first_name:
            return self.last_name + ' - ' + self.first_name + ' [ ' + self.address + ' ]'
        else:
            return self.email + ' - ' + self.telephone

class Commands(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    panner = models.ForeignKey(Panner, on_delete=models.CASCADE)
    deliverance = models.BooleanField("With deliverance ?", default=False)
    status = models.BooleanField("is Done ?", default=False)
    created_at = models.DateTimeField("Created at", auto_now=True)

    def __str__(self):
        return 'Commands for ' + self.client.telephone + ' - ' + self.client.email + ' [ ' + self.client.address + ' ] '