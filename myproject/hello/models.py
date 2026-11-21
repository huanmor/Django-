from django.db import models
# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100, verbose_name="活动标题")   #短文本
    description = models.TextField(blank=True, verbose_name="活动简介")#长文本
    start_time = models.DateTimeField(verbose_name="开始时间")
    location = models.CharField(max_length=100, verbose_name="活动地点")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

class Meta:
    ordering = ["-start_time"]

def str_(self):
    return self.title