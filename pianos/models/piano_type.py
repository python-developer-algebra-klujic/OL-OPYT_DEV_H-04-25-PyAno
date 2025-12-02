from django.db import models


class PianoType(models.Model):
    name = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Tip klavira')