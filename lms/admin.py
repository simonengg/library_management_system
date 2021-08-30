from django.contrib import admin
from .models import StudentExtra,IssuedBook, AddBook
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)

@admin.register(AddBook)
class AddBookAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'author', 'isbn']
