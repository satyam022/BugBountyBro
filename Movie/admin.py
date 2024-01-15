from django.contrib import admin

from Movie.models import Movie, Category, Comments, SubComments, News

# Register your models here.

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(SubComments)
admin.site.register(News)

