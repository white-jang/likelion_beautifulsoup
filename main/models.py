from django.db import models

# Create your models here.

# 크롤링한 데이터 넣기
class MelonList(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.name
