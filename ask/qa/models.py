from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title=models.CharField(default="", max_length=255)
    text = models.TextField(default="", max_length=2055)
    addet_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default="", on_delete=models.SET_DEFAULT)
    likes = models.ManyToManyField(User, related_name='q_to_likes')


class Answer(models.Model):
    text = models.TextField(default="", max_length=2055)
    addet_at = models.DateField(blank=True,  auto_now_add=True)
    question = models.ForeignKey(Question, default="", on_delete=models.SET_DEFAULT)
    auther = models.ForeignKey(User,default="", on_delete=models.SET_DEFAULT)


class QuestionManager(models.Manager):

  def new(self):
    return self.order_by('-added_at')

  def popular(self):
    return self.order_by('-rating')
