from django.db import models

from .piano_category import PianoCategory
from .piano_type import PianoType


class Piano(models.Model):
    model = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Naziv klavira')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')

    category = models.ForeignKey(PianoCategory,
                                 null=False,
                                 default=0,
                                 on_delete=models.SET_DEFAULT)

    type = models.ForeignKey(PianoType,
                             null=False,
                             default=0,
                             on_delete=models.SET_DEFAULT)

    picture_url = models.CharField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Upisite link do slike klavira')

    def __str__(self):
        return f'{self.model} ({self.category.name})'
