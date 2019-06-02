from django.db import models

# Create your models here.
class msg(models.Model):
    content = models.TextField(blank=False, null=False)
    name = models.CharField(max_length=25,blank=False)

    def __str__(self):
        return self.name

    #def __str__(self):
        #return self.name
