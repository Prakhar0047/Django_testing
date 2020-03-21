from django.db import models

# Create your models here.

class details(models.Model):
    first_name = models.CharField(max_length = 256, unique = True)
    last_name = models.CharField(max_length = 256, unique = True)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.first_name, self.last_name, self.email