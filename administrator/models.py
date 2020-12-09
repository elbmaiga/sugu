from django.db import models

# Create your models here.

class Category(models.Model):
    TRADER = "TRADER"
    BUSINESSMAN = "BUSINESS MAN"
    CHOICES = [
        ("Trader", TRADER),
        ("Business Man", BUSINESSMAN),
    ]
    category = models.CharField("Admin Category", choices=CHOICES, max_length=15, unique=True)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.category

class Administrator(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("password", max_length=255)
    email = models.EmailField("Email", max_length=30, unique=True)
    telephone = models.CharField("Telephone", max_length=20, unique=True)
    activity_name = models.CharField("Activity Name", max_length=40, unique=True)
    last_name = models.CharField("Last name", max_length=40, blank=True)
    first_name = models.CharField("First name", max_length=40, blank=True)
    date_birth = models.DateField("Birth date")

    def __str__(self):
        return self.username