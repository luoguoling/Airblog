#coding:utf8
from django.conf.urls import *


urlpatterns = patterns('blog.views',
    # Blog 列表页
    url(r'^$', 'article_list',
        {'template_name': 'article_list.html'}, name='articleList'),
    # Blog 详情页面
    url(r'^(?P<id>\d+)/$', 'article_details',
        {'template_name': 'article_details.html'}, name='articleDetails'),
    # Blog 分类过滤
    url(r'^filter/category/(?P<category_id>\d+)/$', 'category_filter', 
        {'template_name': 'article_list.html'}, name='categoryFilter'),
    # Blog 标签过滤
    url(r'^filter/tag/(?P<tag_id>\d+)/$', 'tag_filter',
        {'template_name': 'article_list.html'}, name='tagFilter'),
)
