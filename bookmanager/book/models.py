from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "peopleinfo"
        verbose_name = '人物信息'