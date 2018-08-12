from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)  #定义类型，字符串，最长255
    img_url = models.URLField() #类型，网址
    rate = models.IntegerField()  #类型，数字

    #d新增一个外键字段，models.CASCADE，表示如果self被删除，这个字段会被跟着删除
    childs = models.ForeignKey('self',related_name='father',blank=True,null=True,on_delete=models.CASCADE)

    #将每一条数据的标题名称显示为电影名w
    def __str__(self):
        return self.movie_name
