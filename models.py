from django.db import models


# Create your models here.
class Block(models.Model):
    number = models.IntegerField()
    cost = models.FloatField()
    entrances = models.IntegerField()
    floors = models.IntegerField()
    apartments_per_block = models.IntegerField()

    def __str__(self):
        return {self.number} - {self.cost}


class Owner(models.Model):
    name = models.CharField(max_length=200, null=True)
    purchase_date = models.DateField()
    types = (('1', "Выкуп"), ('2', "Выкуп не до конца"), ('3', "Расторгнуто"), ('4', "Не продано"),)
    status = models.CharField(choices=types, max_length=128)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    sqmeter = models.FloatField()

    def __str__(self):
        return {self.name} - {self.block}
