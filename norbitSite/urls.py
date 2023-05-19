from django.urls import path
from norbitSite.views import IndexView, SingleBlog, projects, contact, Blogs, aboutus

app_name = 'norbitSite'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/<int:pk>', SingleBlog.as_view(), name="single-blog"),
    path('projeler/', projects, name='projects'),
    path('iletisim/', contact, name='contact'),
    path('bloglar/', Blogs.as_view(), name='blogs'),
    path('hakkımızda/', aboutus, name='about-us'),
]