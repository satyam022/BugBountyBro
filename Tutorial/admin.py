from django.contrib import admin

from embed_video.admin import AdminVideoMixin
from .models import Tutorial_course, Course_category, Problam, News


# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Tutorial_course, MyModelAdmin)
admin.site.register(Course_category)
admin.site.register(Problam)
admin.site.register(News)



