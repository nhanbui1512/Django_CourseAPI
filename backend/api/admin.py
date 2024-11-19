from django.contrib import admin

from . models import Category, Course, Lession, User, Tag


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lession)
admin.site.register(User)
admin.site.register(Tag)
