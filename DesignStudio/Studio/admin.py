from django.contrib import admin
from .models import *

admin.site.register(AdvUser)
admin.site.register(Application)
admin.site.register(Category)


#@admin.register(Application)
#class ApplicationsAdmin(admin.ModelAdmin):
    #list_display = ('title', 'description', 'category')