from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Movie

def index(request,name):
    #name是需要在网址中输入的内容，可以随便输入

    #获取要查询的电影
    movie = name
    print(movie)
    #打开excel,数据存储库
    lines = ['蛮荒故事 Relates salvajes','肖申克的救赎 Relates salvajes']

    #查询
    for line in lines:
        if movie in line:
            # return HttpResponse(line)
            context = {'tip': line,'sayhi': 'hello!'}
            return render(request, 'movie/index.html', context)
    fo =  'for'

    #传递变量，可以一次传递多个变量
    """
    1、index.html中使用方式： {{ tip }}
    2、如果变量不多，可以直接放入render作为第三个参数
       
    """
    # context = }
    # return render(request, 'movie/index.html', context)


    return render(request, 'movie/index.html', {'tip': '没有该电影', 'sayhi': '很遗憾，我们会尽快添加！'})

def add(request):

    ## 往数据库中新增一条数据
    # mv = Movie.objects.create(
    #     movie_name = '蛮荒故事 Relates salvajes',
    #     img_url = 'https://movie.douban.com/subject/24750126/',
    #     rate = 19,
    # )

    # 获取这个数据数组的名字，第一个数组的值
    mv = Movie.objects.filter(movie_name='肖申克')[0]
    c1 = Movie.objects.filter(movie_name='楚门的世界')[0]
    c2 = Movie.objects.filter(movie_name='心灵捕手')[0]

    #改变mv其中一个字段的值
    mv.childs = c1
    mv.childs = c2

    #保存mv中的改变,只会保存最后一个
    mv.save()


    return render(request, 'movie/index.html', {'tip': '哈哈'})



    # 怎么使用html文件
    """
    1、如果需要运行html,必须把建立的app，加入setting.py的‘NSTALLED_APPS’列表中
    2、在app下面，建立templates文件夹，直接放，直接只用'index.html',或者继续加子目录，前面就需要加上路径
    
    """


# orm，可以数据映射不同类型的数据库，包括sqlite,mysql,oracal
# 数据库相关文件，应该放在models.py