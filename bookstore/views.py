from django.shortcuts import render
from .models import Book
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def all_book(request):
    print("---------------------------------------------")

    all_book = Book.objects.filter(isactive=True)
    # print(all_book[0].id)
    # length = len(all_book)
    return render(request,"bookstore/all_book.html",locals())
    # return HttpResponse("test book is ok")


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    # return HttpResponse("这是测试页面%s"%id)
    except Exception as e:
        print("error is %s"%e)
        return HttpResponse("---当前书籍不存在---")
    if request.method == "GET":
        return render(request,"bookstore/update_book.html",locals())
    elif request.method == "POST":
        price = request.POST["price"]
        market_price = request.POST["market_price"]

        book.price = price
        book.market_price = market_price
        book.save()

        return HttpResponseRedirect("/bookstore/all_book")


def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id,isactive=True)
    except Exception as e:
        print("error is %s" % e)
        return HttpResponse("---当前书籍不存在---")

    book.isactive=False
    book.save()
    return HttpResponseRedirect("/bookstore/all_book")

