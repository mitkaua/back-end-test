from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_simple'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^article/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^', 'article.views.articles'),
)
