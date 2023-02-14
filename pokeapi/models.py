from django.db import models


class Pokemon(models.Model):
    creature_id = models.IntegerField(null=True, help_text="ID number assigned by Kaggle.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    primary_type = models.CharField(max_length=255)
    secondary_type = models.CharField(max_length=255, null=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField(null=True)
    legendary = models.BooleanField(default=False)
