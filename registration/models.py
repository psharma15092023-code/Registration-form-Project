from django.db import models

# # Create your models here.
class registration(models.Model):
    Firstname=models.TextField()
    Lastname=models.TextField(default="")
    EmailAddress=models.EmailField()
    Phone=models.CharField()
    City=models.CharField()
    Country=models.CharField()
    
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"
    
    