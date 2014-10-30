from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify


class Candidate(models.Model):
    roll = models.CharField(max_length=9 , unique = True)#CharField?
    cat = models.IntegerField(default=0)
    ds = models.BooleanField(default=False)
    pd = models.BooleanField(default=False)
    #slug = models.SlugField(unique=True)
    # program=models.Field(max_length=4,min_length=4)
#     institue=models.CharField(max_length=1)
    
    def __str__(self):
        return self.roll
        
    #def save(self, *args, **kwargs):
     #           self.slug = slugify(self.name)
      #          super(Candidate, self).save(*args, **kwargs)

    
class Preference(models.Model):
    candidate = models.ForeignKey(Candidate)
    institute = models.CharField(max_length=1)
    program = models.CharField(max_length=4)
    class Meta:
         unique_together = (("candidate","program"))
################################################################
#tut models below
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
# class Rank(models.Model):
#     code=models.CharField