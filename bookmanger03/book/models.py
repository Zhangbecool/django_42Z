from django.db import models

# Create your models here.


class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True, null=False)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        db_table = 'bookinfo'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'[{self.id}, {self.name}, {self.pub_date}, {self.readcount}, {self.commentcount}, {self.is_delete}]'


class PeopleInfo(models.Model):

    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'[{self.id}, {self.name}, {self.gender}, {self.description}, {self.is_delete}, {self.book}]'

    class Meta:
        verbose_name = '人物信息'
        verbose_name_plural = '人物信息'
        db_table = 'peopleinfo'
