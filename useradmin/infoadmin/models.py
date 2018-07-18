from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100) # port
    password = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    crt_date = models.DateTimeField()
    due_date = models.DateTimeField()
    price = models.CharField(max_length=10)
    tag = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username
