from django.db import models

# Create your models here.

class Question(models.Model) :
    question_text = models.CharField(max_length=200);
    pub_feild = models.DateTimeField('Published_date');

class Choice(models.Model) :
    question = models.ForeignKey(Question);
    choice_text = models.CharField(max_length=200);
    votes = models.IntegerField(default=0)
