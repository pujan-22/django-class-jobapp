from django.contrib import admin
from app.models import JobPost


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "salary", "date")
    list_filter = ("date", "salary", "expiry")
    search_fields = ("title", "salary", "description")
    search_help_text = "Write query and hit enter"
    # fields = (('title', 'description'), 'salary')
    # exclude = ('title', )
    fieldsets = (
        ('Basic Information',{
            'fields':('title', 'description')
        }),
        ('More Information',{
            'classes':('collapse', ),
            'fields':(('expiry','salary'),'slug')
        })
    )
    
# Register your models here.
admin.site.register(JobPost, JobAdmin)