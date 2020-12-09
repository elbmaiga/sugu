from django.db import models

from administrator.models import Administrator
# Create your models here.

class Category(models.Model):
    ALIMENTATION = "ALIMENTATION"
    MODE = "MODE"
    INFORMATIC = "INFORMATIC"
    SPORT = "SPORTS & HEALTH"
    CHOICES = [
        ("Alimentation", ALIMENTATION),
        ("Mode", MODE),
        ("Informatic", INFORMATIC),
        ("Sports-Health", SPORT),
    ]
    category = models.CharField("Category article", choices=CHOICES, max_length=40, unique=True)
    description = models.TextField("Description", blank=True)

    def __str__(self):
         return self.category

class Images(models.Model):
    image = models.ImageField(upload_to="articles/")
    
    #class Meta:
       # abstract = True

class Articles(models.Model):
    FCFA = "XOF"
    EUR = "EUR"
    DOL = "DOL"
    DEVISE = [
        ("FCFA", FCFA),
        ("EUR", EUR),
        ("DOL", DOL),
    ]
    category = models.ManyToManyField(Category, related_name="Category")
    users = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=255)
    price = models.IntegerField("Price")
    description = models.TextField("Description", default="N/A")
    cover = models.ImageField(upload_to="articles/")
    images = models.ManyToManyField(to=Images, related_name='Images', blank=True)
    devise = models.CharField("Devise", max_length=10, choices=DEVISE, default=FCFA)
    available = models.BooleanField("is Available", default=True)
    star = models.BooleanField("is Star ?", default=False)
    promo = models.BooleanField("is in Promo ?", default=False)
    promo_price = models.IntegerField("Promo price", default=0)
    slug = models.SlugField("Slug", max_length=255, unique=True)
    created_at = models.DateTimeField("Created at", auto_now=True)

    def __str__(self):
        return self.title