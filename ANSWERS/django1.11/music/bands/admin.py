from django.contrib import admin

from .models import Band, Member, Genre

admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Genre)
