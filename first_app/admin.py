from django.contrib import admin

# Register your models here.
from first_app.models import Students, Enrollments, Courses


admin.site.register(Courses)
admin.site.register(Enrollments)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'age')
    list_filter = ('name', 'created_at')
    list_editable = ('age',)


admin.site.register(Students, StudentsAdmin)

# admin.site.register(Students)
