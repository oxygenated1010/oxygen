from django.contrib import admin
from .models import Postdata, Category, Profile, Comment

# Register your models here.
admin.site.register(Postdata)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)