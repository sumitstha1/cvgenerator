from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    dob = models.DateField(max_length=50)
    quali = models.CharField(max_length=50)
    hobby = models.CharField(max_length=200)
    objective = models.CharField(max_length=1000)

    class Meta:
        db_table = 'pt_cv_user'