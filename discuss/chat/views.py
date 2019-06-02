from django.shortcuts import render
from .models import msg
from .forms import  ConForm


# Create your views here.
def home(request):
    msgs = msg.objects.all()
    if request.method == 'POST':
        form = ConForm(request.POST)
        form.save()#adding to database


    form = ConForm()
    message = []


    for talk in msgs:

        message.insert(0,talk)


    context = {'message' : message, 'form' : form}#sending a reference to index.html

    return render(request, 'index.html' , context)
