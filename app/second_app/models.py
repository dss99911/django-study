import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


def selectData():
    current_year = timezone.now().year
    Question.objects.all()  # get all
    Question.objects.filter(id=1)

    # get single. if not exists, raise exception
    Question.objects.get(pub_date__year=current_year)
    Question.objects.get(id=2)
    Question.objects.get(pk=2)  # primary key. same with `id=2`


def orderBy():
    Question.objects.order_by('-pub_date')[:5]


def createModifyData():
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    q.question_text = "ddd"
    q.save()


def deleteData():
    Question.objects.get(id=2).delete()


def foreignSet():
    current_year = timezone.now().year

    q = Question.objects.get(pk=1)
    q.choice_set.all()  # as Choice has question for foreign key. it's available to search choices of question

    # create
    c = q.choice_set.create(choice_text='Not much', votes=0)
    Choice.objects.filter(question__pub_date__year=current_year)
