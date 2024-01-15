from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from Movie.models import Movie, Category, SubComments, Comments, News


# Create your views here.


def Movies(request):
    movie = Movie.objects.all()
    news=News.objects.all()
    if request.method == "GET":
        st = request.GET.get('query')
        if st != None:
            movie = Movie.objects.filter(title__icontains=st)

    paginator = Paginator(movie, 9)
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
        'movie':postpage,
        'news':news
    }
    return render(request, 'movies/movie.html', data)


@login_required(login_url='login')
def Movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    list = Category.objects.all()

    if request.method == 'POST':
        comm = request.POST.get('comm')
        comm_id = request.POST.get('comm_id')  # None

        if comm_id:
            SubComments(movie=movie,
                        user=request.user,
                        comm=comm,
                        comment=Comments.objects.get(id=int(comm_id))
                        ).save()
        else:
            Comments(movie=movie, user=request.user, comm=comm).save()

    comment = []
    for c in Comments.objects.filter(movie=movie):
        comment.append([c, SubComments.objects.filter(comment=c)])

    data = {

        'comments': comment,
        'movie': movie,
        'list': list,
    }

    return render(request, 'movies/moviesdetails.html', data)


def Movie_category(request,slug):
    cat = get_object_or_404(Category, slug=slug)

    cours = Movie.objects.filter(category=cat)
    data = {

        'cat': cat,
        'cours': cours
    }
    return render(request, 'movies/movie_category.html',data)

