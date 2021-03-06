from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.utils import timezone
from.models import Post,Author,Category
from django.views.generic import DetailView,ListView
from django.db.models import Q,Count
from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CreatForm
from pprint import pprint


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'search.html', context)
    

def home(request):
    context={
        'posts': Post.objects.all(),
        'latest_posts':Post.objects.order_by('-timestamp')[0:3],
        'authors':Author.objects.all()
        }
    return render(request,'index.html',context)





class Post_Create(CreateView):
    template_name = "create.html"
    form_class = CreatForm
    def post(self,request):
        form = CreatForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect("home")
        return render(request,'create.html')

        





    #fields = ['title','categories','content','file','thumbnail','author','suggestion_first','suggestion_second','suggestion_third','suggestion_fourth','suggestion_fifth','suggestion_sixth','suggestion_seventh' ]
    



class Post_detail(DetailView):
    model = Post
    template_name = 'preview.html' 
    
    def get_context_data(self, *args, **kwargs): 
        context = super(Post_detail, 
             self).get_context_data(*args, **kwargs)       
        return context 


class Author_detail(DetailView):
    model = Author
    template_name = 'profile.html'



