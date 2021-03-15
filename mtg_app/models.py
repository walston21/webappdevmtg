from django.db import models

# Create your models here.

class MTGCard(models.Model):
    name = models.CharField(max_length=50)
    colors = models.CharField(max_length=10)
    mana_cost = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name