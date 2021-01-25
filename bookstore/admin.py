from django.contrib import admin
from .models import Book,Author
# Register your models here.


class BookManager(admin.ModelAdmin):
    list_display = ["id","title","price","market_price","pub"]
    list_display_links = ["id","title"]
    list_filter = ["pub",]
    search_fields = ["id","title","desc"]
    list_editable = ["price"]

class AuthorManager(admin.ModelAdmin):
    list_display = ["id","name","age","email"]
    list_display_links = ["id","name"]


admin.site.register(Book,BookManager)
admin.site.register(Author,AuthorManager)