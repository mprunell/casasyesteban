from django.contrib import admin
from solo.admin import SingletonModelAdmin
from pages.models import (Person, Image, Carousel,
                          ContentMeta, Content, Quote,
                          Home, About, Work, Consultancy,
                          Contact, Workshop, Workshops)


admin.site.register(Person)
admin.site.register(Image)
admin.site.register(Carousel)
admin.site.register(Quote)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Work)
admin.site.register(Consultancy)
admin.site.register(Workshop)
admin.site.register(Workshops)
admin.site.register(Contact)



