from django.db import models
from django.utils import timezone

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default='Without title')
    intro = models.CharField('Intro', max_length=200)
    whole_text = models.TextField('Article')
    created_date = models.DateTimeField('Date of create', default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
