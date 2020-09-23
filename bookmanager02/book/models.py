from django.db import models

# Create your models here.


class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True, null=False)
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{},{},{},{},{},{}".format(self.id, self.name, self.pub_date, self.readcount, self.commentcount, self.is_delete)



class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, default='')
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '[{},{},{},{},{}]'.format(self.name, self.gender, self.description, self.is_delete, self.book)
