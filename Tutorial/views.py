from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Tutorial.models import Tutorial_course, Course_category, Problam, News


# Create your views here.


def Tutorial(request):
    cours = Tutorial_course.objects.all()
    news=News.objects.all()
    if request.method == "GET":
        st = request.GET.get('query')
        if st != None:
            cours = Tutorial_course.objects.filter(topic__icontains=st)

    paginator = Paginator(cours, 9)
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
        'cours': postpage,
        'news':news
    }
    return render(request, 'tutorials/tutorial.html', data)


@login_required(login_url='login')
def Course(request, slug):
    cours = get_object_or_404(Tutorial_course, slug=slug)
    cat = Course_category.objects.all()
    if request.method == "POST":
        name = request.POST['username']
        problem = request.POST['problem']
        describe_problem = request.POST['describe_problem']
        if len(name) < 2 or len(problem) < 3 or len(describe_problem) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            problam = Problam(username=name, problam=problem, describe_problem=describe_problem)
            problam.save()
            messages.success(request, "Your problem has been successfully submit")

            # return redirect('tutorials/course_details.html')
    data = {

        'cours': cours,
        'cat': cat,

    }

    return render(request, 'tutorials/course_details.html', data)


def Category_course(request,pk):
    cat = get_object_or_404(Course_category, pk=pk)

    cours = Tutorial_course.objects.filter(category=cat)
    data = {

        'cat': cat,
        'cours':cours
    }
    return render(request, 'tutorials/Course_category.html', data)

