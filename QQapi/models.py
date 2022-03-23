from django.db import models


# Create your models here.
class Chat_record(models.Model):
    name = models.CharField(max_length=100)
    re_name = models.CharField(max_length=100)
    message = models.TextField()
    robot = models.CharField(max_length=100)
    QQ = models.IntegerField(max_length=64)
    re_QQ = models.IntegerField(max_length=64)
    send_time = models.IntegerField(max_length=64)

