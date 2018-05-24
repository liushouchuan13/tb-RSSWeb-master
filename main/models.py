from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RSS(models.Model):
    """ RSS """
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128, verbose_name="rss标题")
    link = models.CharField(max_length=512, verbose_name="rss链接")
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title
