from django.contrib import admin

# Register your models here.
from image_cropping import ImageCroppingMixin
from website.models import Staff, Class, SimplePage, FontPageSlide

admin.site.register(Class)


class ImageCroppingAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Staff, ImageCroppingAdmin)

admin.site.register(SimplePage, ImageCroppingAdmin)

admin.site.register(FontPageSlide, ImageCroppingAdmin)