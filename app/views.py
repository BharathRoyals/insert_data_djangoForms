from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            Tid=TFD.cleaned_data['Tid']
            Name=TFD.cleaned_data['Name']
            Age=TFD.cleaned_data['Age']
            Email=TFD.cleaned_data['Email']
            Date=TFD.cleaned_data['Date']
            
            
            TO=Topic.objects.get_or_create(Tid=Tid,Name=Name,Age=Age,Email=Email,Date=Date)[0]
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topics.html',d1)

    return render(request,'insert_topic.html',d)

def display_topics(request):
    return render(request,'display_topics')