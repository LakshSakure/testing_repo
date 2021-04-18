from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    add_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "tbl_users"