from django.db import models
from image_cropping import ImageRatioField


class Staff(models.Model):
    url = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    sort_order = models.PositiveSmallIntegerField(default=500)
    bio_image = models.ImageField(null=True)
    cropped = ImageRatioField('bio_image', '400x400')

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


class SimplePage(models.Model):
    url = models.CharField(max_length=100, help_text="The url to use (everything after ltjjc.com).")
    header_text = models.CharField(max_length=45, help_text="The text that will be shown bold at the top of the page")
    body = models.TextField(help_text="The body of the page")
    image = models.ImageField(upload_to='spi')
    cropped = ImageRatioField('image', '400x400')

    def __unicode__(self):
        return self.url


class FontPageSlide(models.Model):
    header = models.CharField(null=True, blank=True, max_length=50, help_text="The large text displayed on the slide.")
    subtext = models.CharField(null=True, blank=True, max_length=100, help_text="The smaller text shown under the large"
                                                                                "text on the slide.")
    navigate_to = models.CharField(max_length=50,null=True, blank=True, help_text="The link to display with the "
                                                                                  "\"continue reading\" sign. "
                                                                                  "Can be blank")
    image = models.ImageField(upload_to='slide')
    cropped = ImageRatioField('image', '930x375')
    sort_order = models.IntegerField(default=500)

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ['sort_order']