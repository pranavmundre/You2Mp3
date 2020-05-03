from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
	url(r'^$',views.home,name='homepage'),
	url(r'^home',views.about,name='homepage'),
	url(r'^search/',include('search.urls',namespace='search')),
	url(r'^admin/', admin.site.urls),
    url(r'^download/(?P<path>.*)/(?P<path2>.*)$',views.download),
    url(r'^robots\.txt$',TemplateView.as_view(template_name="seo/robots.txt", content_type='text/plain')),
    url(r'^forum/',views.forum),
    url(r'^share/(?P<path>.*)$',views.share),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
