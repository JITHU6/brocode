from django.shortcuts import render,get_object_or_404
from subscribe.forms import Subscribe
# from home.models import Blog,Category
# Create your views here.
def home(request):
    sub = Subscribe()
    return render(request, 'home/index.html', {'form':sub})
def about(request):
    return render(request, 'about/about.html')
#
# def blog(request):
#     # posts= Blog.objects.all()
#     return render(request, 'blog/blog.html', {
#             'post': Blog.objects.all()
#         })
#
# def blogdetails(request, slug=None):
#
#     return render(request, 'blog/single-blog.html', {
#         'post': get_object_or_404(Blog, slug=slug),
#     })
def project(request):

    return render(request, 'project/project.html')
def contact(request):
    sub= Subscribe()
    return render(request, 'contact/contact.html',{'form':sub})
#
# def services(request):
#
#     return render(request, 'services/services.html')


    # return render(request, 'blog/single-blog.html')

# def view_category(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    return render(request,'view_category.html', {
#        'category': category,
#        'posts': Blog.objects.filter(category=category)[:5]
#    })