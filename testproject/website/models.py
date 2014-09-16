from django.db import models
# Create your models here.
#from ltjjc.settings import MEDIA_ROOT


class Staff(models.Model):
    url = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    sort_order = models.PositiveSmallIntegerField(default=500)
    bio_image = models.ImageField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Staff"

class Class(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=25)
    instructor = models.ForeignKey(Staff)
    description = models.TextField(null=True)
    sort_order = models.PositiveSmallIntegerField(default=500)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"
