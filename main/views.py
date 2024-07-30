from django.shortcuts import render
from .models import Text

# Create your views here.
def maintainence(request):
    text = Text.objects.all()
    return render(request, 'index.html', {'text': text})