from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, SubComment, Comment, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def Home(request):
    post = Post.objects.all()
    news=News.objects.all()
    if request.method == "GET":
        st = request.GET.get('query')
        if st != None:
            post = Post.objects.filter(title__icontains=st)

    paginator = Paginator(post, 6)
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
        'post': postpage,
        'news':news,
        # 'postpage': postpage,

    }

    return render(request, 'blogs/home.html', data)


@login_required(login_url='login')
def Details(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    cat = Category.objects.all()

    if request.method == 'POST':
        comm = request.POST.get('comm')
        comm_id = request.POST.get('comm_id')  # None

        if comm_id:
            SubComment(post=post,
                       user=request.user,
                       comm=comm,
                       comment=Comment.objects.get(id=int(comm_id))
                       ).save()
        else:
            Comment(post=post, user=request.user, comm=comm).save()

    comments = []
    for c in Comment.objects.filter(post=post):
        comments.append([c, SubComment.objects.filter(comment=c)])

    data = {

        'comments': comments,
        'post': post,
        'cat': cat,

    }

    return render(request, 'blogs/blog.html', data)


def CategoryList(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.filter(status=Post.ACTIVE)

    data = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'blogs/category.html', data)


def Page404(request):
    return render(request, '404_page.html')

