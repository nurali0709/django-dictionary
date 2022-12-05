from django.db import models
from django.forms import ModelForm
LANG_CHOICES = [
    ['Turkmen', "Turkmen"],
    ['English', "English"],
]

class Word(models.Model):
    title = models.CharField('Word', max_length=255)
    description = models.TextField('Description')
    lang = models.CharField('Lang', max_length=255, choices = LANG_CHOICES, default = "Turkmen")
    
    def __str__(self):
        return self.title

