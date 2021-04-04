from django.contrib import admin

from .models import Articles

admin.site.site_header = "Articles Admin"
admin.site.title = "Articles Area"


admin.site.register(Articles)
