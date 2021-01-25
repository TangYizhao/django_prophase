from django.urls import path

from bookstore import views

urlpatterns = [

    path("all_book/",views.all_book),

    path("update_book/<int:book_id>",views.update_book, name = "update_book"),

    path("delete_book/<int:book_id>",views.delete_book, name = "delete_book"),
]
