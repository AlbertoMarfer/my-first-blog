from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
#from .forms import PostForm, PostSchool
from .forms import PostSchool
from .models import School

# Create your views here.

##
##def post_list(request):
##    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
##    return render(request, 'blog/post_list.html', {'posts': posts})
##
##def post_detail(request, pk):
##    post = get_object_or_404(Post, pk=pk)
##    return render(request, 'blog/post_detail.html', {'post': post})
##
##def post_new(request):
##    if request.method == "POST":
##        form = PostForm(request.POST)
##        if form.is_valid():
##            post = form.save(commit=False)
##            post.author = request.user
##            post.published_date = timezone.now()
##            post.save()
##            return redirect('post_detail', pk=post.pk)
##    else:
##        form = PostForm()
##    return render(request, 'blog/post_edit.html', {'form': form})
##
##def post_edit(request, pk):
##    post = get_object_or_404(Post, pk=pk)
##    if request.method == "POST":
##        form = PostForm(request.POST, instance=post)
##        if form.is_valid():
##            post = form.save(commit=False)
##            post.author = request.user
##            post.published_date = timezone.now()
##            post.save()
##            return redirect('post_detail', pk=post.pk)
##    else:
##        form = PostForm(instance=post)
##    return render(request, 'blog/post_edit.html', {'form': form})
##
def school_new(request):
    if request.method == "POST":
        form = PostSchool(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            school.created_date = timezone.now()
            school.save()
            return redirect('school_detail', pk=school.pk)
    else:
        form = PostSchool()
    return render(request, 'blog/school_edit.html', {'form': form})

def school_edit(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "POST":
        form = PostSchool(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            school.created_date = timezone.now()
            school.save()
            return redirect('school_detail', pk=school.pk)
    else:
        form = PostSchool(instance=school)
    return render(request, 'blog/school_edit.html', {'form': form})


def school_list(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box', None)
        schools = School.objects.filter(name=search_query)
    else:
        schools = School.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/school_list.html', {'schools': schools})


def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'blog/school_detail.html', {'school': school})


