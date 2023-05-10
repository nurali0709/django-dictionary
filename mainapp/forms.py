from django.forms import ModelForm
from .models import Word
from django import forms

class WordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Word
        fields = ['lang', 'title']

class WordAdd(forms.ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()

    class Meta:
        model = Word
        fields = ['title', 'description', 'lang']
