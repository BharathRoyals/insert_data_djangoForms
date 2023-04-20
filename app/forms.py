from django import forms
class TopicForm(forms.Form):
    Tid=forms.IntegerField()
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Email=forms.EmailField()
    Date=forms.DateTimeField()
    