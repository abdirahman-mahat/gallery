from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def gallery(request):
    images = Image.all_images()
    return render(request, 'gallery.html', {"images":images})


def search_results(request):

    if 'image' in request.GET and request.GET("image"):
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "No photos under this category exist"
        return render(request, 'search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})