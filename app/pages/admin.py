from django.contrib import admin
from solo.admin import SingletonModelAdmin
from pages.models import Image, Carousel, Page, Home


admin.site.register(Image)
admin.site.register(Carousel)
admin.site.register(Page)
admin.site.register(Home)


