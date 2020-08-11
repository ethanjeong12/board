from django.db import models

class Contents(models.Model):

    nickname = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    date     = models.DateField(auto_now_add = True)
    content  = models.TextField()
    user     = models.ForeignKey("user.Users", on_delete = models.CASCADE)

    class Meta:
        db_table = "contents"
