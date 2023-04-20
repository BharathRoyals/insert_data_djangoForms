from django.db import models

# Create your models here.
class Topic(models.Model):
    Tid=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(default=18)
    Email=models.EmailField()
    Date=models.DateField()
    
    

    def __str__(self):
        return self.Name
    

