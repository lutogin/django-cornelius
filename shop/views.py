from django.shortcuts import render, get_object_or_404


def index(req):
    """Индексная страница"""
    return render(req, '')
