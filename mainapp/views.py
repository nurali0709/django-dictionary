import logging
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import modelform_factory
from .models import Word
from .forms import *



def index(request):
    word_form = WordForm(request.POST)
    if request.method == "POST" and word_form.is_valid():
        argument = word_form.cleaned_data["title"]
        lang = word_form.cleaned_data["lang"]
        if argument == "":
            return render(request, 'base.html')
        words_list = Word.objects.filter(title__contains = argument, lang = lang)
        old_word = argument
        return render(request, 'base.html', {'words_list' : words_list, "old_word":old_word, 'word_form': word_form})
    else:
        word_form = modelform_factory(Word, form = WordForm)
        return render(request, 'base.html', {'word_form': word_form})