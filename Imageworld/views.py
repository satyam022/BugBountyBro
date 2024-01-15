from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Imageworld.form import ImageForm
from Imageworld.models import Image


# Create your views here.


def Image_world(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    image = Image.objects.all()
    if request.method == "GET":
        st = request.GET.get('query')
        if st != None:
            image = Image.objects.filter(title__icontains=st)

    paginator = Paginator(image, 9)
    page_number = request.GET.get('page')
    try:
        postpage = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        postpage = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        postpage = paginator.page(paginator.num_pages)
    data = {
        'image': postpage,
        'form': form,
    }
    return render(request, 'imageworld/image.html', data)

