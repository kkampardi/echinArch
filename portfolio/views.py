from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Project

def home(request):
    return  render( request, 'home.html', {} )

def about(request):
    return render( request, 'about.html', {} )

def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})


def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    #grub all the uploads set for current project
    uploads = project.uploads.all()
    #grub all categories set for current project
    categories = project.category.all()
    #grub all tags set for current project
    tags = project.tag.all()

    #get projects for similar porjects
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')

    return render(request, 'portfolio/portfolio_detail.html',
    {
        'project': project,
        'uploads': uploads,
        'categories': categories,
        'tags': tags,
        'projects': projects,

    })

def contact(request):
    return render( request, 'contact.html', {})

def post_list(reguest):
    posts = Post.objects.filter(publish__lte=timezone.now().order_by('publish'))
    return render(request, 'blog/blog_list.html', {'post': post })
