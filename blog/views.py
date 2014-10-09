#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
# 模型相关导入
from blog.models import (Category, Tag, Author, Article)


def get_context(request):
    '''
    The global context of blog sidebar
    '''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recently = Article.objects.all()[:10]

    return {'CATEGORIES': categories, 'TAGS': tags,
        'RECENTLY': recently,
    }

def article_list(request, template_name):
    '''Get all the blog'''
    articles = Article.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request, processors=[get_context]))

def article_details(request, template_name, id=''):
    ''' According to the id to the corresponding blog'''
    try:
        article = Article.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    article_tags = article.tags.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request, processors=[get_context]))

def category_filter(request, template_name, category_id):
    '''A specified class of blogs'''
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise Http404
    articles = category.article_set.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request, processors=[get_context]))

def tag_filter(request, template_name, tag_id):
    '''A specified tag blogs'''
    try:
        tag = Tag.objects.get(id=tag_id)
    except Tag.DoesNotExist:
        raise Http404
    articles = tag.article_set.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request, processors=[get_context]))
