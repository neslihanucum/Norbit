from django.shortcuts import render
from django.views.generic import DetailView, ListView
from norbitSite.models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        post = Post.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["post"] = post
        return context


class SingleBlog(DetailView):
    model = Post
    template_name = 'single-blog.html'


def projects(request):
    return render(request, 'projects.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def aboutus(request):
    return render(request, 'about-us.html', {})


class Blogs(ListView):
    model = Post
    template_name = 'blogs.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        post = Post.objects.all()
        context = super(Blogs, self).get_context_data(*args, **kwargs)
        context["post"] = post
        return context