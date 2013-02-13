from django.conf.urls.defaults import patterns, url

from views import GalleryView, GalleryDetailView, GalleryByAuthorView, GalleryThumbnailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery-detail'),
    url(r'^thumbnail/$', GalleryThumbnailView.as_view(), name='gallery-thumbnail'),
    url(r'^byauthor/(?P<authorname>\w+)/$', GalleryByAuthorView.as_view(), name='gallery-byauthor'),
)
