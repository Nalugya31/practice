from django.db import models

class Biodata(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    email = models.EmailField()

    def _str_(self):
        return f'{self.first_name} {self.last_name}'
