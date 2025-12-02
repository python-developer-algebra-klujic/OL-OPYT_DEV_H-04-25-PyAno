from django.db import models


class PianoCategory(models.Model):
    name = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Kategorija klavira')
