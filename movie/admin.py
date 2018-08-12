from django.contrib import admin

from .models import Movie


# 给管理员账户注册Movie
# Register your models here.
admin.site.register(Movie)


