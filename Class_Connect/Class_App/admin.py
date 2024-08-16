from django.contrib import admin
from.models import Contact,Enrollment,trainer,course,studyresources,Notice,Query_Doubt


# Register your models here.
admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(Enrollment)
admin.site.register(trainer)
admin.site.register(course)
admin.site.register(studyresources)
admin.site.register(Query_Doubt)





admin.site.site_header="Class Connect Admin dashboard"
admin.site.site_title="Class Connect"
admin.site.index_title="Start Your Class"

class Contact_Admin(admin.ModelAdmin):
    list_display=['name','email','question']