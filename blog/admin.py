#!/usr/bin/env python
#coding:utf8

from django.contrib import admin
from blog.models import (Author, Article, Category, Tag,
                          Images, Files)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


class ImagesAdmin(admin.StackedInline):
    model = Images
    admin.site.register(Images)


class FilesAdmin(admin.StackedInline):
    model = Files
    admin.site.register(Files)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    raw_id_fields = ('author',)

    inlines = [ImagesAdmin, FilesAdmin]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Tag)
