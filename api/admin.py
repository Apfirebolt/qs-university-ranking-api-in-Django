from django.contrib import admin
from . models import CustomUser, Application


admin.site.register(CustomUser)
admin.site.register(Application)
admin.site.site_header = "QS World Ranking Admin"
admin.site.site_title = "QS World Ranking Admin Portal"
admin.site.index_title = "Welcome to QS World Ranking Admin Portal"
