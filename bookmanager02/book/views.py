from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            'log': '都有网特',
            'name': 'zhangbecool',
            
            }
    return render(request, 'book/index.html', context)



from book.models import BookInfo, PeopleInfo
PeopleInfo.objects.all()
BookInfo.objects.all()


# 查询编号为1的图书
BookInfo.objects.get(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=False)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 3, 5))
from django.db.models import Q
BookInfo.objects.filter(Q(id=1) | Q(id=3) | Q(id=5))
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')
from django.db.models import F
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
# 查询编号不等于3的图书。
BookInfo.objects.filter(~Q(id=3))

from django.db.models import Sum, Avg, Max, Min, Count
# 查询图书的总阅读量
BookInfo.objects.aggregate(Sum('readcount'))
# 查询图书总数
BookInfo.objects.count()

BookInfo.objects.order_by('readcount')

BookInfo.objects.order_by('-readcount')

# 查询书籍为1的所有人物信息
PeopleInfo.objects.filter(book=1)
book = BookInfo.objects.get(id=1)
book.peopleinfo_set()
# 查询人物为1的书籍信息
people = PeopleInfo.objects.get(id=1)
people.book

# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
BookInfo.objects.get(name='天龙八部').peopleinfo_set.all()
PeopleInfo.objects.filter(book__name='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)
books = BookInfo.objects.filter(readcount__gt=30)
a = [book.peopleinfo_set.all() for book in books]
print(a)


# 惰性

books = BookInfo.objects.all()
[book.id for book in books]