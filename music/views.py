from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is a Music App Home Page")

def detail(request, album_id):
        return HttpResponse("<h2> Details of Album id: " + str(album_id)+ "<h2>")
