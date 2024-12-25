from django.http import HttpResponse
from django.shortcuts import render

def show_basic(requset):
    return HttpResponse('Получилось запустить через убунту!')
