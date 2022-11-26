from django.contrib import admin
from Standup.models import Books
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display=["id","Bname","Bauthor","YearofPub","Price","Page","Category"]
admin.site.register(Books,BooksAdmin)
