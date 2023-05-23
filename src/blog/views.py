from django.http import Http404 
from django.shortcuts import render, get_object_or_404

# Create your views here.
from.models import Blogpost 


# GET -> 1 object
# filter -> [] objects

def blog_post_detail_page(request, slug):
    print("DJANGO SAYS", request.method, request.path, request.user)
    # obj = Blogpost.object.get(slug=slug)
       # queryset = Blogpost.objects.filter(slug=slug)
       # if queryset.count() == 0:
       #     raise Http404
       # obj = queryset.first()
    obj = get_object_or_404(Blogpost, id=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    
    return render(request, template_name, context)

# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / DELETE 

# Create Retrieve Update Delete

def blog_post_list_view(request):
    qs = Blogpost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj,}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj}
    return render(request, template_name, context)
