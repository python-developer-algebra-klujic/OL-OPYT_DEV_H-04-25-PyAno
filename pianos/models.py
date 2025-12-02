from django.db import models

# Create your models here.
class Piano(models.Model):
    model = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Naziv klavira')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')


class PianoType(models.Model):
    name = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Tip klavira')


class PianoCategory(models.Model):
    name = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Kategorija klavira')
