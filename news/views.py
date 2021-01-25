from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def index_view(request):
    # return HttpResponse("---this is news index---")
    return render(request,"news/index.html")