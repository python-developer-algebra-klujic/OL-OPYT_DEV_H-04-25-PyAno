from django.db import models


class Piano(models.Model):
    model = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Naziv klavira')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')
