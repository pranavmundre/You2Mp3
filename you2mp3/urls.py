from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts' : PostSitemap
}

urlpatterns = [
	url(r'^$',views.home,name='homepage'),
	url(r'^home',views.about,name='homepage'),
	url(r'^search/',include('search.urls',namespace='search')),
	url(r'^admin/', admin.site.urls),
    url(r'^download/(?P<path>.*)/(?P<path2>.*)$',views.download),
    url(r'^robots\.txt$',TemplateView.as_view(template_name="seo/robots.txt", content_type='text/plain')),
    url(r'^sitemap\.xml$',TemplateView.as_view(template_name="seo/sitemap.xml",content_type='text/xml')),
    url(r'^forum/',views.forum),
    url(r'^share/(?P<path>.*)$',views.share),
    url(r'^serviceworker\.js$',TemplateView.as_view(template_name="seo/serviceworker.js", content_type='text/javascript')),
    url(r'^manifest\.json$',TemplateView.as_view(template_name="seo/manifest.json", content_type='application/manifest+json')),
    url(r'blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^tinymce/', include('tinymce.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

