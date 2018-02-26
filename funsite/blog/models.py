from django.db import models


#for each column specify column name, 
#specify the datatype
#any contonstrants of the data type
class Post(models.Model):
    title= models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField()
    
    def __str__(self):
        return self.title
    