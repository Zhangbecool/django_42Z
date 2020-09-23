from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            'log': '都有网特',
            'name': 'zhangbecool',
            
            }
    return render(request, 'book/index.html', context)


def center(request):
    from book.models import BookInfo, PeopleInfo
    PeopleInfo.objects.all()
    BookInfo.objects.all()


    # 查询编号为1的图书
    BookInfo.objects.get(id=1)
    # 查询书名包含'湖'的图书
    BookInfo.objects.filter()
    # 查询书名以'部'结尾的图书
    # 查询书名为空的图书
    # 查询编号为1或3或5的图书
    # 查询编号大于3的图书
    # 查询1980年发表的图书
    # 查询1990年1月1日后发表的图书
