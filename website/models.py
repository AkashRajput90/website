from django.db import models

# Create your models here.
class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
        
