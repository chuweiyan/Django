import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Population(models.Model):
    id = models.AutoField(primary_key=True)  # 自增，且为主键
    population = models.BigIntegerField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)  # 返回的不是字符串,需要加上str

    def query_population_count(self):
        return self.population


class Video(models.Model):
    region = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    view_num = models.CharField(max_length=200)
    danmu = models.CharField(max_length=200)
    update_time = models.DateTimeField(auto_now_add=True)
    up_author = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    video_source = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'polls_video'

    def __str__(self):
        return str(self.title)  # 返回的不是字符串,需要加上str


class PollsVideo(models.Model):
    region = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    title = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    view_num = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    danmu = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    up_author = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    video_url = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    video_source = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'polls_video'
