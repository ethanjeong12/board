from django.db import models

class Users(models.Model):

    user_id  = models.CharField(max_length = 50, null = True)
    password = models.CharField(max_length = 200)
    email    = models.EmailField(max_length = 200)
    nickname = models.CharField(max_length = 50)
    is_admin = models.BooleanField(default = False)
    
    class Meta:
        db_table = "users"
