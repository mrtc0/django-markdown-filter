from django.shortcuts import render
from app.models import Post


def index(request):
    p = Post.objects.get(pk=1)
    return render(request, 'index.html', {'p': p})
