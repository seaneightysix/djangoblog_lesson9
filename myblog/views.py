from django.shortcuts import render, redirect
from myblog.models import Genre, Post
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from myblog.forms import MyPostForm
from django import forms
from django.utils import timezone

def add_post(request):
 
    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.created_date = timezone.now()
            model_instance.modified_date = model_instance.created_date
            model_instance.published_date = model_instance.created_date
            model_instance.save()
            return redirect('/')
 
    else:
        form = MyPostForm()
        return render(request, "post_form.html", {'form': form})


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)

def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    
    except Post.DoesNotExist:
    	raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)

def get_genres(request, genre):
	try:
		genre_pk = Genre.objects.get(genre=genre)
		results = Post.objects.all()
		results = results.filter(genre = genre_pk)
		
	except Post.DoesNotExist:
    	 raise Http404	

	context = {'results': results,
			   'genre': genre
			  }
	return render(request, 'genre_list.html', context)